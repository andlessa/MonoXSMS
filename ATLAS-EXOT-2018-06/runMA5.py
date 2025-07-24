#!/usr/bin/env python3

# Run MadAnalysis5 for already generated hepmc files

import sys,os,glob
import pyslha
import xml.etree.ElementTree as ET
import subprocess, logging, shutil
import multiprocessing
import tempfile
import time, datetime
from configParserWrapper import ConfigParserExt

FORMAT = '%(levelname)s in %(module)s.%(funcName)s(): %(message)s at %(asctime)s'
logging.basicConfig(format=FORMAT,datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger("MA5Scan")

logger.info("Hello!")


def getDataFromBanner(banner):
    with open(banner, 'r') as f:
        lines = f.readlines()
        
    isxsecBlock = False
    xsec = None
    xsecBlock = []

    for i, line in enumerate(lines):
        if '<MGGenerationInfo>' in line:
            isxsecBlock = True
            continue
        elif '</MGGenerationInfo>' in line:
            isxsecBlock = False
            continue
        if isxsecBlock:
            xsecBlock.append(line)

    xsec_str = xsecBlock[-1].strip('\n').split(' ')[-1]
    xsec = float(xsec_str)

    f.close()

    xtree = ET.parse(banner)
    xroot = xtree.getroot()
    slha = xroot.find('header').find('slha').text
    pars = pyslha.readSLHA(slha)

    if 55 in pars.blocks['MASS']:
        model = 'spin1'
        mMed = pars.blocks['MASS'][55]

    elif 54 in pars.blocks['MASS']:
        model = 'spin0'
        mMed = pars.blocks['MASS'][54]

    elif 2000002 in pars.blocks['MASS']:
        model='tchannel'
        mMed = pars.blocks['MASS'][2000002]

    if model in ['spin1','spin0']:
        mDM = pars.blocks['MASS'][52]
    elif model in ['tchannel']:
        mDM = pars.blocks['MASS'][57]
    else:
        mDM = None

    ma5Folder_name = None

    if model == 'spin1':
        gVq = pars.blocks['DMINPUTS'][4] # Mediator-quark vector coupling
        gAq = pars.blocks['DMINPUTS'][10] # Mediator-quark axial coupling
        gVx = pars.blocks['DMINPUTS'][2] # Mediator-DM vector coupling
        gAx = pars.blocks['DMINPUTS'][3] # Mediator-DM axial coupling
        if (gAq != 0) and (gAx != 0):
            ma5FolderName = 'dma_%i_%i'%(mDM, mMed)
        else:
            ma5FolderName = 'dmv_%i_%i'%(mDM, mMed)

    elif model == 'spin0':
        gVq = pars.blocks['DMINPUTS'][6] # Mediator-quark scalar coupling
        gAq = pars.blocks['DMINPUTS'][12] # Mediator-quark pseudoscalar coupling
        gVx = pars.blocks['DMINPUTS'][3] # Mediator-DM scalar coupling
        gAx = pars.blocks['DMINPUTS'][4] # Mediator-DM pseudoscalar coupling
        if (gAq != 0) and (gAx != 0):
            ma5FolderName = 'dmp_%i_%i'%(mDM, mMed)
        else:
            ma5FolderName = 'dms_%i_%i'%(mDM, mMed)

    elif model == 'tchannel':
        # print(pars.blocks['DMS3U'][1,1])
        lam = pars.blocks['DMS3U'][1,1]
        ma5FolderName = 'dmys3u1_%i_%i'%(mDM, mMed)

    return xsec, ma5FolderName


def createCommandsFile(parser):
    """
    Creates the command file for MadAnalysis5 based on parameters passed by user.

    :param parder: dictionary with parser sections

    :return: True if command file creation is successful, otherwise returns False.
    """

    pars = parser['MA5Pars']
    sets = parser['MA5Set']
    ma5Options = parser['options']
    anaFolder = pars['anaFolder']

    mg5Folder = pars['mg5Folder']
    banners = sorted(glob.glob(os.path.dirname(mg5Folder+'/Events/run_*/')+'/*banner.txt'),key=os.path.getmtime,reverse=False)

    if len(banners) == 0:
        logger.info('No banners were found, not using cross-section value.')
    
    # create commands file
    commandsFile = pars['commandsFile']
    storeRoot = ma5Options['storeRoot']
    ma5CardPath = pars['ma5CardPath']

    with open(commandsFile, 'w') as f:
        f.write(f'set main.recast = on\n')
        f.write(f'set main.recast.store_root = {storeRoot}\n')
        f.write(f'set main.recast.card_path = {ma5CardPath}\n')
        if 'lumi' in sets:
            lumi = sets['lumi']
            f.write(f'set main.recast.add.extrapolated_luminosity = {lumi}\n')

    hempcFiles = sorted(glob.glob(os.path.dirname(mg5Folder+'/Events/run_*/')+'/*hepmc.gz'),key=os.path.getmtime,reverse=False)
    
    with open(commandsFile, 'a') as f:
        for i, file in enumerate(hempcFiles):
            if len(banners) == 0:
                f.write(f'import {file} as ana_{i}\n')
            else: 
                xsec, folderName =  getDataFromBanner(banners[i])
                f.write(f'import {file} as {folderName}\n')
                f.write(f'set {folderName}.xsection = {xsec}\n')
                print(f'\n{folderName}, xsec: {xsec} pb\n')
        f.write(f'submit {anaFolder}')
    f.close()

    return commandsFile, folderName

def runMA5(parser):

    t0 = time.time()

    commandsFile, folderName = createCommandsFile(parser)

    pars = parser['MA5Pars']

    logger.info('Generating process using %s' %commandsFile)

    #Generate process
    ma5Folder = os.path.abspath('/home/ramos/madanalysis5-1_11_0')
    run = subprocess.Popen('./bin/ma5 -R -s %s' %commandsFile,shell=True,
                                stdout=subprocess.PIPE,stderr=subprocess.PIPE,
                                cwd=ma5Folder)

    output,errorMsg = run.communicate()
    logger.debug('MA5 process error:\n %s \n' %errorMsg)
    logger.debug('MA5 process output:\n %s \n' %output)
    logger.info('Finished MadAnalysis5 processes.')

    runInfo = {'time (s)': time.time() - t0}
    runInfo.update({'processFolder': folderName})
    runInfo.update(pars)

    return runInfo



def main(parfile, verbose):
    level = verbose
    levels = {'debug': logging.DEBUG,
              'info': logging. INFO,
              'warn': logging.WARNING,
              'error': logging.ERROR}
    
    if not level in levels:
        logger.error(f'Unknown log level "{level}" supplied.')
        sys.exit()

    logger.setLevel(level = levels[level])

    parser = ConfigParserExt(inline_comment_prefixes='#')
    ret = parser.read(parfile)

    if ret == []:
        logger.error(f'No such file or directory: "{args.parfile}"')

    #Get a list of parsers (in case loops have been defined)    
    parserList = parser.expandLoops()

    now = datetime.datetime.now()
    for irun, newParser in enumerate(parserList):
        mg5Folder = newParser.get('MA5Pars','mg5Folder')
        mg5Folder = os.path.abspath(mg5Folder)

        if mg5Folder[-1] == '/':
            mg5Folder = mg5Folder[:-1]
        if not os.path.isdir(mg5Folder):
            logger.error(f'Folder {mg5Folder} not found!')
            sys.exit()

        parserDict = newParser.toDict(raw=False)
        logger.debug('submitting with pars:\n %s \n' %parserDict)
        output = runMA5(parserDict)    

#     Wait for jobs to finish:
    logger.info("Finished analyzing all samples at %s" %(now.strftime("%Y-%m-%d %H:%M")))

    return output

if __name__ == '__main__':

    import argparse
    ap = argparse.ArgumentParser( description=
            "Run a (serial) MadAnalysis5 scan for the parameters defined in the parameters file." )
    ap.add_argument('-p', '--parfile', default='scan_parameters.ini',
            help='path to the parameters file [scan_parameters.ini].')
    ap.add_argument('-v', '--verbose', default='info',
            help='verbose level (debug, info, warning or error). Default is info')


    t0 = time.time()

    args = ap.parse_args()
    output = main(args.parfile,args.verbose)
            
    print("\n\nDone in %3.2f min" %((time.time()-t0)/60.))




        
        
