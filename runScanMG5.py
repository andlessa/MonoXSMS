#!/usr/bin/env python

#Uses an input SLHA file to compute cross-sections using MadGraph and the UFO model files
#The calculation goes through the following steps
# 1) Run MadGraph using the options set in the input file 
# (the proc_card.dat, parameter_card.dat and run_card.dat...).
# Madgraph is used to compute the widths and cross-sections
# 2) Run slhaCreator to extract the information of the MadGraph output
# and generate a SLHA file containing the cross-sections

#First tell the system where to find the modules:
from __future__ import print_function
import sys,os
from configParserWrapper import ConfigParserExt
import logging,shutil
import subprocess
import tempfile
import time,datetime

FORMAT = '%(levelname)s in %(module)s.%(funcName)s(): %(message)s at %(asctime)s'
logging.basicConfig(format=FORMAT,datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger("MG5Scan")



def getProcessCard(parser):
    """
    Create a process card using the user defined input.
    If a proccard has been defined and it already exists, it will use it instead.
    
    :param parser: ConfigParser object with all the parameters needed
    
    :return: The path to the process card
    
    """
    
    pars = parser.toDict(raw=False)["MadGraphPars"]
    
    if 'proccard'in pars:
        processCard = pars['proccard']     
        if os.path.isfile(processCard):
            logger.debug('Process card found.')
            #Make sure the output folder defined in processCard matches the one defined in processFolder:
            pcF = open(processCard,'r')
            cardLines = pcF.readlines()
            pcF.close()
            outFolder = [l for l in cardLines if 'output' in l and 'output' == l.strip()[:6]]            
            if outFolder:
                outFolder = outFolder[0]
                outFolder = outFolder.split('output')[1].replace('\n','').strip()
                outFolder = os.path.abspath(outFolder)
                if outFolder != os.path.abspath(pars['processFolder'].strip()):
                    logger.debug("Folder defined in process card does not match the one defined in processFolder. Will use the latter.")
                pcF = open(processCard,'w')
                for l in cardLines:
                    if (not 'output' in l) or (not 'output' == l.strip()[:6]):
                        pcF.write(l)
                    else:
                        pcF.write('output %s \n' %os.path.abspath(pars['processFolder']))
                pcF.close()
            if not outFolder:
                pcF = open(processCard,'a')
                pcF.write('output %s \n' %os.path.abspath(pars['processFolder']))
                
            return processCard
        
    else:
        processCard = tempfile.mkstemp(suffix='.dat', prefix='processCard_', 
                                   dir=pars['MG5path'])
        os.close(processCard[0])
        processCard = processCard[1]
        
    processCardF = open(processCard,'w')
    processCardF.write('import model sm \n')
    processCardF.write('define p = g u c d s u~ c~ d~ s~ \n')
    processCardF.write('import model %s \n' %os.path.abspath(parser.get('options','modelFolder')))     
    xsecPDGList = parser.get('options','computeXsecsFor')
    ufoFolder =  parser.get('options','modelFolder')
    processes = defineProcesses(xsecPDGList, ufoFolder)
    for iproc,proc in enumerate(processes):
        processCardF.write('add process %s @ %i \n' %(proc,iproc))
    
    l = 'output %s\n' %os.path.abspath(pars['processFolder'])
    processCardF.write(l)
    processCardF.write('quit\n')
    processCardF.close()
    
    return processCard

def generateProcesses(parser):
    """
    Runs the madgraph process generation.
    This step just need to be performed once for a given
    model and set of processes, since it is independent of the 
    numerical values of the model parameters.
    
    :param parser: ConfigParser object with all the parameters needed
    
    :return: True if successful. Otherwise False.
    """
    
    
    #Get run folder:
    processCard = os.path.abspath(getProcessCard(parser))
    pars = parser.toDict(raw=False)["MadGraphPars"]
    
    #Generate process
    logger.info('Generating process using %s' %processCard)
    run = subprocess.Popen('./bin/mg5_aMC -f %s' %processCard,shell=True,
                                stdout=subprocess.PIPE,stderr=subprocess.PIPE,
                                cwd=pars['MG5path'])
         
    output,errorMsg = run.communicate()
    logger.debug('MG5 process error:\n %s \n' %errorMsg)
    logger.debug('MG5 process output:\n %s \n' %output)
    logger.info("Finished process generation")
        
    return True

def generateEvents(parser):
    
    """
    Runs the madgraph event generation.
    
    :param parser: ConfigParser object with all the parameters needed
    
    :return: True if successful. Otherwise False.
    """

    t0 = time.time()
    
    pars = parser.toDict(raw=False)["MadGraphPars"]
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

    pythia8File = os.path.join(processFolder,'Cards/pythia8card.dat')
    delphesFile = os.path.join(processFolder,'Cards/delphes_card.dat')
    if 'delphescard' in pars and os.path.isfile(pars['delphescard']):
        shutil.copyfile(pars['delphescard'],delphesFile)
    elif os.path.isfile(delphesFile):
        os.remove(delphesFile)

    if 'pythia8card' in pars and os.path.isfile(pars['pythia8card']):
        shutil.copyfile(pars['pythia8card'],pythia8File) 
    elif os.path.isfile(pythia8File):
        os.remove(pythia8File)
        os.remove(delphesFile)

    #Generate commands file:       
    commandsFile = tempfile.mkstemp(suffix='.txt', prefix='MG5_commands_', dir=processFolder)
    os.close(commandsFile[0])
    commandsFileF = open(commandsFile[1],'w')
    commandsFileF.write('0\n')
    comms = parser.toDict(raw=False)["MadGraphSet"]
    #Set a low number of events, since it does not affect the total cross-section value
    #(can be overridden by the user, if the user defines a different number in the input card)
    for key,val in comms.items():
        commandsFileF.write('set %s %s\n' %(key,val))

    #Done setting up options
    commandsFileF.write('done\n')

    commandsFileF.close()
    commandsFile = commandsFile[1]      
    
    logger.info("Generating MG5 events with command file %s" %commandsFile)
    run = subprocess.Popen('./bin/generate_events < %s' %(commandsFile),
                           shell=True,stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,cwd=processFolder)
      
    output,errorMsg= run.communicate()
    logger.debug('MG5 event error:\n %s \n' %errorMsg)
    logger.debug('MG5 event output:\n %s \n' %output)
      
    logger.info("Finished event generation in %1.2f min" %((time.time()-t0)/60.))
    
    return True
    

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

    now = datetime.datetime.now()
    for i,newParser in enumerate(parserList):
        r = generateEvents(newParser)
        logger.info("Finished run %i/%i at %s" %(i,len(parserList),now.strftime("%Y-%m-%d %H:%M")))


    logger.info("Finished all runs (%i) at %s" %(len(parserList),now.strftime("%Y-%m-%d %H:%M")))
    


if __name__ == "__main__":
    
    import argparse    
    ap = argparse.ArgumentParser( description=
            "Run a (serial) MadGraph scan for the parameters defined in the parameters file." )
    ap.add_argument('-p', '--parfile', default='scan_parameters.ini',
            help='path to the parameters file [scan_parameters.ini].')
    ap.add_argument('-v', '--verbose', default='error',
            help='verbose level (debug, info, warning or error). Default is error')


    t0 = time.time()

    args = ap.parse_args()
    output = main(args.parfile,args.verbose)
            
    print("\n\nDone in %3.2f min" %((time.time()-t0)/60.))
