#!/usr/bin/env python3

#Uses an input SLHA file to compute cross-sections using MadGraph and the UFO model files
#The calculation goes through the following steps
# 1) Run MadGraph using the options set in the input file 
# (the proc_card.dat, parameter_card.dat and run_card.dat...).

from __future__ import print_function
import sys,os,glob
from configParserWrapper import ConfigParserExt
import logging,shutil
import subprocess
import multiprocessing
import tempfile
import time,datetime

FORMAT = '%(levelname)s in %(module)s.%(funcName)s(): %(message)s at %(asctime)s'
logging.basicConfig(format=FORMAT,datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger("MG5Scan")

def generateProcess(parser):
    """
    Runs the madgraph process generation.
    This step just need to be performed once for a given
    model, since it is independent of the 
    numerical values of the model parameters.
    
    :param parser: Dictionary with parser sections.
    
    :return: True if successful. Otherwise False.
    """
    
    
    #Get run folder:    
    pars = parser["MadGraphPars"]
    processCard = os.path.abspath(pars["proccard"])    
    if not os.path.isfile(processCard):
        logger.error("Process card %s not found" %processCard)
        raise ValueError()

    processFolder = os.path.abspath(pars["processFolder"])
    if os.path.isdir(processFolder):
        logger.warning("Process folder %s found. Skipping process generation." %processFolder)
        return False

    logger.info('Generating process using %s' %processCard)

    # Create copy of process card to replace output folder
    procCard = tempfile.mkstemp(suffix='.dat', prefix='procCard_')
    os.close(procCard[0])
    procCard = procCard[1]
    shutil.copy(processCard,procCard)
    with open(procCard,'r') as f:
        lines = f.readlines()
    lines = [l for l in lines[:] if l.strip()[:6] != 'output']
    lines.append('output %s\n' %processFolder)
    with open(procCard,'w') as f:
        for l in lines:
            f.write(l)
    
    #Generate process
    mg5Folder = os.path.abspath('./MG5')
    run = subprocess.Popen('./bin/mg5_aMC -f %s' %procCard,shell=True,
                                stdout=subprocess.PIPE,stderr=subprocess.PIPE,
                                cwd=mg5Folder)
         
    output,errorMsg = run.communicate()
    logger.debug('MG5 process error:\n %s \n' %errorMsg)
    logger.debug('MG5 process output:\n %s \n' %output)
    logger.info("Finished process generation")

    os.remove(procCard)
        
    return True

def getInfoFromOutput(outputStr):
    """
    Try to fetch the run name, the number of events
    and the total cross-section from the MG5 output.

    :param outputStr: String containing the MG5 output

    :return: Dictionary with run summary
    """

    outputStr = str(outputStr)
    # Get summary block
    summaryBlock = outputStr.split("Results Summary for run")[-1]
    summaryBlock = summaryBlock.split("Done")[0]
    # Split block into lines
    summaryLines = [l for l in summaryBlock.split('\\n') if l.strip()]
    # Get info from lines:
    xsec, runNumb, runTag, nevts = None,None,None,None
    for l in summaryLines:
        if 'tag' in l:
            runNumb,runTag = l.split('tag:')
            runNumb = runNumb.replace(':','').replace('=','').strip()
            runTag = runTag.replace(':','').replace('=','').strip()
        elif 'cross-section' in l.lower():
            xsec = eval(l.lower().split(':')[1].split('+-')[0])
        elif 'events'in l.lower():
            nevts = eval(l.lower().split(':')[1])

    runInfo = {'run number' : runNumb, 'run tag' : runTag, 
               'cross-section (pb)' : xsec, 'Number of events' : int(nevts)}
    return runInfo

def generateEvents(parser):
    
    """
    Runs the madgraph event generation.
    
    :param parser: Dictionary with parser sections.
    
    :return: True if successful. Otherwise False.
    """

    t0 = time.time()
    
    pars = parser["MadGraphPars"]
    if not 'processFolder' in pars:
        logger.error('Process folder not defined.')
        return False        
    else:
        processFolder = pars['processFolder']
            
    if not os.path.isdir(processFolder):
        logger.error('Process folder %s not found.' %processFolder)
        return False

    if 'runcard' in pars and os.path.isfile(pars['runcard']):    
        shutil.copyfile(pars['runcard'],os.path.join(processFolder,'Cards/run_card.dat'))
    if 'paramcard' in pars and os.path.isfile(pars['paramcard']):
        shutil.copyfile(pars['paramcard'],os.path.join(processFolder,'Cards/param_card.dat'))    


    # By default do not run Pythia or Delphes
    runPythia = parser['options']['runPythia']
    runDelphes = parser['options']['runDelphes']

    pythia8File = os.path.join(processFolder,'Cards/pythia8_card.dat')
    delphesFile = os.path.join(processFolder,'Cards/delphes_card.dat')
    if runDelphes and 'delphescard' in pars:
        if os.path.isfile(pars['delphescard']):
            shutil.copyfile(pars['delphescard'],delphesFile)

    if runPythia and 'pythia8card' in pars:        
        if os.path.isfile(pars['pythia8card']):
            shutil.copyfile(pars['pythia8card'],pythia8File) 
    
    #Generate commands file:       
    commandsFile = tempfile.mkstemp(suffix='.txt', prefix='MG5_commands_', dir=processFolder)
    os.close(commandsFile[0])
    commandsFileF = open(commandsFile[1],'w')
    if runPythia:
        commandsFileF.write('shower=Pythia8\n')
    else:
        commandsFileF.write('shower=OFF\n')
    if runDelphes:
        commandsFileF.write('detector=Delphes\n')
    else:
        commandsFileF.write('detector=OFF\n')

    commandsFileF.write('done\n')
    comms = parser["MadGraphSet"]
    #Set a low number of events, since it does not affect the total cross-section value
    #(can be overridden by the user, if the user defines a different number in the input card)
    for key,val in comms.items():
        commandsFileF.write('set %s %s\n' %(key,val))

    #Done setting up options
    commandsFileF.write('done\n')
    commandsFileF.write('done\n')

    commandsFileF.close()
    commandsFile = commandsFile[1]      
    
    logger.info("Generating MG5 events with command file %s" %commandsFile)
    run = subprocess.Popen('./bin/generate_events --multicore --nb_core=1 < %s' %(commandsFile),
                           shell=True,stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,cwd=processFolder)
      
    output,errorMsg= run.communicate()
    runInfo = {}
    runInfo.update(pars)
    # Try to get info from output
    try:
        runInfo.update(getInfoFromOutput(output))
    except:
        pass

    logger.debug('MG5 event error:\n %s \n' %errorMsg)
    logger.debug('MG5 event output:\n %s \n' %output)
      
    logger.info("Finished event generation in %1.2f min" %((time.time()-t0)/60.))
    os.remove(commandsFile)

    cleanOutput = parser['options']['cleanOutput']
    if cleanOutput and runInfo:
        lheFile = os.path.join(processFolder,'Events',runInfo['run number'],'unweighted_events.lhe.gz')
        logger.debug('Removing  %s' %lheFile)
        if os.path.isfile(lheFile):
            os.remove(lheFile)
        hepmcFile = os.path.join(processFolder,'Events',runInfo['run number'], '%s_pythia8_events.hepmc.gz'  %runInfo['run tag'])
        logger.debug('Removing  %s' %hepmcFile)
        if os.path.isfile(hepmcFile):
            os.remove(hepmcFile)

    return runInfo

def moveFolders(runInfo):
    """
    Move the run folders from the temporary running folder
    to the process folder.
    """

    # Get run folder:
    runFolder = runInfo['runFolder']
    runNumber = runInfo['runNumber']
    eventFolder = os.path.join(runInfo['processFolder'],'Events')

    for runDir in glob.glob(os.path.join(runFolder,'Events','run_*')):
        shutil.move(runDir,os.path.join(eventFolder,'run_%02d' %runNumber))

    shutil.rmtree(runFolder)


def main(parfile,verbose):
   
    level = verbose
    levels = { "debug": logging.DEBUG, "info": logging.INFO,
               "warn": logging.WARNING,
               "warning": logging.WARNING, "error": logging.ERROR }
    if not level in levels:
        logger.error ( "Unknown log level ``%s'' supplied!" % level )
        sys.exit()
    logger.setLevel(level = levels[level])    

    parser = ConfigParserExt(inline_comment_prefixes="#")   
    ret = parser.read(parfile)
    if ret == []:
        logger.error( "No such file or directory: '%s'" % args.parfile)
        sys.exit()
            
    #Get a list of parsers (in case loops have been defined)    
    parserList = parser.expandLoops()

    # Start multiprocessing pool
    ncpus = -1
    if parser.has_option("options","ncpu"):
        ncpus = int(parser.get("options","ncpu"))
    if ncpus  < 0:
        ncpus =  multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=ncpus)

    now = datetime.datetime.now()
    children = []
    run0 = 0
    for irun,newParser in enumerate(parserList):
        processFolder = newParser.get('MadGraphPars','processFolder')
        if not os.path.isdir(processFolder):
            logger.info('Folder %s not found. Running MG5 to create folder.' %processFolder)
            generateProcess(newParser)

        # Get largest existing events folder:
        eventsFolder = os.path.join(processFolder,'Events')
        if os.path.isdir(eventsFolder):
            for runF in glob.glob(os.path.join(eventsFolder,'run*')):
                run0 = int(os.path.basename(runF).replace('run_',''))+1

        # Create temporary folders
        runFolder = tempfile.mkdtemp(dir=os.path.dirname(processFolder), 
                                     prefix='%s_',suffix='_run_%02d' %run0+irun)

        newParser.set('MadGraphPars','runFolder',runFolder)
        newParser.set('MadGraphPars','runNumber',run0+irun)

        parserDict = newParser.toDict(raw=False)
        p = pool.apply_async(generateEvents, args=(parserDict,irun), callback=moveFolders)                       
        children.append(p)

#     Wait for jobs to finish:
    output = [p.get() for p in children]
    logger.info("Finished all runs (%i) at %s" %(len(parserList),now.strftime("%Y-%m-%d %H:%M")))

    return output
    


if __name__ == "__main__":
    
    import argparse    
    ap = argparse.ArgumentParser( description=
            "Run a (serial) MadGraph scan for the parameters defined in the parameters file." )
    ap.add_argument('-p', '--parfile', default='scan_parameters.ini',
            help='path to the parameters file [scan_parameters.ini].')
    ap.add_argument('-v', '--verbose', default='info',
            help='verbose level (debug, info, warning or error). Default is info')


    t0 = time.time()

    args = ap.parse_args()
    output = main(args.parfile,args.verbose)
            
    print("\n\nDone in %3.2f min" %((time.time()-t0)/60.))
