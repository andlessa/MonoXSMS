#!/usr/bin/env python3

import os, sys, glob, copy
import numpy as np
import pandas as pd
import pyslha
import xml.etree.ElementTree as ET

    
def getModelDict(inputFile):

    # cmsColumns = ['Coupling', 'Mode', '$m_{med}$', '$M_{D}$' '$m_{DM}$', '$g_{DM}$', '$g_{q}$', '$\Gamma_{med}$']
    modelDict = {}

    banner = sorted(glob.glob(os.path.dirname(inputFile[0])+'/*banner.txt'),key=os.path.getmtime,reverse=True)
    if len(banner) == 0:
        print('Banner not found for %s.' %inputFile[0])
        return None
    elif len(banner) > 1:
        print('\n%i banner files found for %s.' %(len(banner), os.path.dirname(inputFile[0])))
        matches = [set(os.path.basename(inputFile[0])).intersection(set(os.path.basename(b))) for b in banner]
        banner = banner[np.argmax(matches)]
        print('Using banner %s' %banner)
    else:
        banner = banner[0]
    
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
    # elif 5000039 in pars.blocks['MASS']:
    #    model = 'ADD'
    #    mMed = pars.blocks['MASS'][5000039]

    if model in ['spin1', 'spin0']:
        mDM = pars.blocks['MASS'][52]
    else:
        mDM = None

    if model == 'spin1':
        gVq = pars.blocks['DMINPUTS'][4] # Mediator-quark vector coupling
        gAq = pars.blocks['DMINPUTS'][10] # Mediator-quark axial coupling
        gVx = pars.blocks['DMINPUTS'][2] # Mediator-DM vector coupling
        gAx = pars.blocks['DMINPUTS'][3] # Mediator-DM axial coupling
        gammaMed = pars.decays[55].totalwidth  # Mediator total width

    elif model == 'spin0':
        gVq = pars.blocks['DMINPUTS'][6] # Mediator-quark scalar coupling
        gAq = pars.blocks['DMINPUTS'][12] # Mediator-quark pseudoscalar coupling
        gVx = pars.blocks['DMINPUTS'][3] # Mediator-DM scalar coupling
        gAx = pars.blocks['DMINPUTS'][4] # Mediator-DM pseudoscalar coupling
        gammaMed = pars.decays[54].totalwidth # Mediator total width

    # elif model == 'ADD':
    #     MD = pars.blocks['ADDINPUTS'][1] # Fundamental Planck scale in large extra dimensions
    #     d = pars.blocks['ADDINPUTS'][2] # Number of extra dimentions

    # Store data 
    if model in ['spin1','spin0']:
        if gVx != 0:
            if model == 'spin1':
                modelDict['Coupling'] = 'Vector'
            elif model == 'spin0':
                modelDict['Coupling'] = 'Scalar'
        else:
            if model == 'spin1':
                modelDict['Coupling'] = 'Axial'
            elif model == 'spin0':
                modelDict['Coupling'] = 'Pseudoscalar'
    # elif model == 'ADD':
    #     modelDict['Coupling'] = 'ADD'
        
    modelDict['Mode'] = 'DM+QCDjets'

    if model in ['spin1','spin0']:
        modelDict['$m_{med}$'] = mMed
        modelDict['$m_{DM}$'] = mDM
        modelDict['$\Gamma_{med}$'] = gammaMed
        if (modelDict['Coupling'] == 'Vector') or (modelDict['Coupling'] == 'Scalar'):
            modelDict['$g_{DM}$'] = gVx
            modelDict['$g_{q}$'] = gVq
        else:
            modelDict['$g_{DM}$'] = gAx
            modelDict['$g_{q}$'] = gAq
    # elif model == 'ADD':
    #     modelDict['$M_{D}$'] = MD
    #     modelDict['$d$'] = d

    return modelDict

if __name__ == '__main__':

    import argparse
    ap = argparse.ArgumentParser(description = 
                                 'Obtain mediator decay width for given banner file.')
    ap.add_argument('-f', '--inputFile', required = True, nargs = '+',
                    help = 'banner file', default = [])
    ap.add_argument('-o', '--outputFile', required = False, help = 'output file.'
                     + 'If not defined, will use the name of the input file.', default = None)

    args = ap.parse_args()
    inputFile = args.inputFile
    outputFile = args.outputFile
    if outputFile is None:
        outputFile = inputFile[0].replace('banner.txt', 'width.pcl')
        # outputFile = outputFile.replace(/[\[\]']+/g,'')

    if os.path.splitext(outputFile)[1] != '.pcl':
        outputFile = os.path.splitext(outputFile)[0]

    modelDict = getModelDict(inputFile)

    df = pd.DataFrame.from_dict(modelDict, orient = 'index').T

    print('Saving to', outputFile)
    df.to_pickle(outputFile)