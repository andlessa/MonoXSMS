#!/usr/bin/env python3

# 1) Run Pythia8 using the options set in the input file 
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
logger = logging.getLogger("PythiaScan")


def generateEvents(parser):
    
    """
    Runs Pythia event generation.
    
    :param parser: Dictionary with parser sections.
    
    :return: True if successful. Otherwise False.
    """

    
    t0 = time.time()

    pars = parser["PythiaPars"]
    outputFolder = pars["outputFolder"]
    outputFile = os.path.join(outputFolder,pars["outputFile"])
    runDelphes = parser['options']['runDelphes']

    pythia8File = os.path.abspath(pars['pythia8card'])
    delphesFile = os.path.abspath(pars['delphescard'])
    cleanOutput = parser['options']['cleanOutput']
    
    #Generate Pythia commands file:       
    commandsFile = tempfile.mkstemp(suffix='.txt', prefix='pythia_cmd_', dir=outputFolder)
    os.close(commandsFile[0])
    commandsFile = commandsFile[1]
    shutil.copyfile(pythia8File,commandsFile)
    commandsFileF = open(commandsFile,'a')
    # Set the Pythia parameters defined in the ini file
    comms = parser["PythiaSet"]
    for key,val in comms.items():
        if "." in key:
            key = "%s:%s" %tuple(key.split('.'))
        commandsFileF.write('%s = %s\n' %(key,val))
    commandsFileF.close()
    
    logger.info("Generating Pythia events with command file %s" %commandsFile)
    run = subprocess.Popen('./main_pythiaADD.exe -c %s -o %s' %(commandsFile,outputFile),
                           shell=True,stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
      
    output,errorMsg= run.communicate()

    logger.debug('Pythia error:\n %s \n' %errorMsg)
    logger.debug('Pythia output:\n %s \n' %output)
    os.remove(commandsFile)

    if runDelphes:
        delphesOutput = outputFile.replace(os.path.splitext(outputFile)[1],'.root')
        delphesFile = os.path.relpath(delphesFile)
        logger.info("Running Delphes with card %s" %delphesFile)
        run = subprocess.Popen('./runDelphesHepMC.sh %s %s %s' %(delphesFile,delphesOutput,outputFile),
                           shell=True,stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
        output,errorMsg= run.communicate()
        logger.debug('Delphes error:\n %s \n' %errorMsg)
        logger.debug('Delphes output:\n %s \n' %output)

        if cleanOutput:
            try:
                os.remove(outputFile)
            except:
                pass


    runInfo = {'time (s)' : time.time()-t0}

    logger.info("Finished run in %1.2f min" %(runInfo['time (s)']/60.))
    return runInfo


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
    if ncpus > len(parserList):
        ncpus = len(parserList)
    pool = multiprocessing.Pool(processes=ncpus)
    if ncpus > 1:
        logger.info('Running in parallel with %i processes' %ncpus)
    else:
        logger.info('Running in series with a single process')

    now = datetime.datetime.now()
    children = []
    for newParser in parserList:
        parserDict = newParser.toDict(raw=False)
        # If run folder does not exist, create it
        outputFolder = parserDict["PythiaPars"]["outputFolder"]
        if not os.path.isdir(outputFolder):
            os.makedirs(outputFolder)
            logger.info("Created output folder %s" %outputFolder)

        logger.debug('submitting with pars:\n %s \n' %parserDict)
        p = pool.apply_async(generateEvents, args=(parserDict,))                       
        children.append(p)

#     Wait for jobs to finish:
    output = [p.get() for p in children]
    logger.info("Finished all runs (%i) at %s" %(len(parserList),now.strftime("%Y-%m-%d %H:%M")))

    return output
    


if __name__ == "__main__":
    
    import argparse    
    ap = argparse.ArgumentParser( description=
            "Run a Pythia scan for the parameters defined in the parameters file." )
    ap.add_argument('-p', '--parfile', default='scan_parameters.ini',
            help='path to the parameters file [scan_parameters.ini].')
    ap.add_argument('-v', '--verbose', default='info',
            help='verbose level (debug, info, warning or error). Default is info')


    t0 = time.time()

    args = ap.parse_args()
    output = main(args.parfile,args.verbose)
            
    print("\n\nDone in %3.2f min" %((time.time()-t0)/60.))
