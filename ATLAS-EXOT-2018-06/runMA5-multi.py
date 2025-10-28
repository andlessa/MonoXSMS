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
    nEvents = None  

    for i, line in enumerate(lines):
        if '<MGGenerationInfo>' in line:
            isxsecBlock = True
            continue
        elif '</MGGenerationInfo>' in line:
            isxsecBlock = False
            continue
        if isxsecBlock:
            xsecBlock.append(line)

    nevts_str = xsecBlock[0].strip('\n').split(' ')[-1]
    nEvents = float(nevts_str)
    xsec_str = xsecBlock[-1].strip('\n').split(' ')[-1]
    xsec = float(xsec_str)

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
        model = 'tchannel'
        mMed = pars.blocks['MASS'][2000002]

    if model in ['spin1','spin0']:
        mDM = pars.blocks['MASS'][52]
    elif model in ['tchannel']:
        mDM = pars.blocks['MASS'][57]
    else:
        mDM = None

    if model == 'spin1':
        gVq = pars.blocks['DMINPUTS'][4]
        gAq = pars.blocks['DMINPUTS'][10]
        gVx = pars.blocks['DMINPUTS'][2]
        gAx = pars.blocks['DMINPUTS'][3]
        if (gAq != 0) and (gAx != 0):
            ma5FolderName = f'dma_{int(mDM)}_{int(mMed)}'
        else:
            ma5FolderName = f'dmv_{int(mDM)}_{int(mMed)}'

    elif model == 'spin0':
        gVq = pars.blocks['DMINPUTS'][6]
        gAq = pars.blocks['DMINPUTS'][12]
        gVx = pars.blocks['DMINPUTS'][3]
        gAx = pars.blocks['DMINPUTS'][4]
        if (gAq != 0) and (gAx != 0):
            ma5FolderName = f'dmp_{int(mDM)}_{int(mMed)}'
        else:
            ma5FolderName = f'dms_{int(mDM)}_{int(mMed)}'

    elif model == 'tchannel':
        lam = pars.blocks['DMS3U'][1,1]
        ma5FolderName = f'dmys3u1_{int(mDM)}_{int(mMed)}'

    return xsec, nEvents, ma5FolderName  



def createCommandsFile(parser):
    """
    Creates the command file for MadAnalysis5 based on parameters passed by user.
    Supports multiple MG5 folders and multiple runs per benchmark.
    Automatically merges samples with identical benchmark names.
    """
    pars = parser['MA5Pars']
    sets = parser['MA5Set']
    ma5Options = parser['options']
    anaFolder = pars['anaFolder']

    mg5Folders = pars['mg5Folder']
    if isinstance(mg5Folders, str):
        mg5Folders = [f.strip() for f in mg5Folders.replace(',', ' ').split()]

    # Structure: benchmark → mg5Folder → list of (xsec, nEvents, hepmc)
    data = {}

    for mg5Folder in mg5Folders:
        mg5Folder = os.path.abspath(mg5Folder)
        banners = sorted(glob.glob(os.path.join(mg5Folder, 'Events/run_*/') + '*banner.txt'))
        hempcFiles = sorted(glob.glob(os.path.join(mg5Folder, 'Events/run_*/') + '*hepmc.gz'))
        
        for banner, hempc in zip(banners, hempcFiles):
            try:
                xsec, nEvents, folderName = getDataFromBanner(banner)
            except Exception as e:
                logger.error(f"Failed to parse {banner}: {e}")
                continue
            if folderName not in data:
                data[folderName] = {}
            if mg5Folder not in data[folderName]:
                data[folderName][mg5Folder] = []
            data[folderName][mg5Folder].append((xsec, nEvents, hempc))

    commandsFile = pars['commandsFile']
    storeRoot = ma5Options['storeRoot']
    ma5CardPath = pars['ma5CardPath']

    with open(commandsFile, 'w') as f:
        f.write('set main.recast = on\n')
        f.write(f'set main.recast.store_root = {storeRoot}\n')
        f.write(f'set main.recast.card_path = {ma5CardPath}\n')
        if 'lumi' in sets:
            f.write(f'set main.recast.add.extrapolated_luminosity = {sets["lumi"]}\n')

        for folderName, folderData in data.items():
            total_xsec = 0
            all_files = []
            for mg5Folder, runs in folderData.items():
                total_events = sum(n for _, n, _ in runs)
                if total_events == 0:
                    continue
                weighted_xsec = sum(x * n for x, n, _ in runs) / total_events
                total_xsec += weighted_xsec
                all_files.extend(h for _, _, h in runs)

            f.write(f'# === {folderName} ===\n')
            for hempc in all_files:
                f.write(f'import {hempc} as {folderName}\n')
            f.write(f'set {folderName}.xsection = {total_xsec}\n')
            logger.info(f'{folderName}: total xsec = {total_xsec:.6f} pb ({len(all_files)} files)\n')

        f.write(f'submit {anaFolder}\n')

    return commandsFile, list(data.keys())[-1] if data else None

def runMA5(parser):

    t0 = time.time()

    commandsFile, folderName = createCommandsFile(parser)

    pars = parser['MA5Pars']

    logger.info('Generating process using %s' %commandsFile)

    #Generate process
    # ma5Folder = os.path.abspath('/home/ramos/madanalysis5-1_11_0')
    # run = subprocess.Popen('./bin/ma5 -R -s %s' %commandsFile,shell=True,
    #                             stdout=subprocess.PIPE,stderr=subprocess.PIPE,
    #                             cwd=ma5Folder)

    # output,errorMsg = run.communicate()
    # logger.debug('MA5 process error:\n %s \n' %errorMsg)
    # logger.debug('MA5 process output:\n %s \n' %output)
    # logger.info('Finished MadAnalysis5 processes.')

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
        mg5FolderList = newParser.get('MA5Pars','mg5Folder')

        for mg5Folder in mg5FolderList:
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




        
        
