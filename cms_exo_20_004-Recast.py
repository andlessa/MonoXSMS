#!/usr/bin/env python3

import os,glob
import numpy as np
import pandas as pd
import glob
import pyslha
import time
import progressbar as P

delphesDir = os.path.abspath("./MG5/Delphes")
os.environ['ROOT_INCLUDE_PATH'] = os.path.join(delphesDir,"external")

import ROOT
import xml.etree.ElementTree as ET


ROOT.gSystem.Load(os.path.join(delphesDir,"libDelphes.so"))

ROOT.gInterpreter.Declare('#include "classes/SortableObject.h"')
ROOT.gInterpreter.Declare('#include "classes/DelphesClasses.h"')
ROOT.gInterpreter.Declare('#include "external/ExRootAnalysis/ExRootTreeReader.h"')


# ### Define dictionary to store data
def getRecastData(inputFile):

    dataDict = {'filename' : os.path.abspath(inputFile)}
    cmsColumns = ['Coupling', 'Mode', '$m_{med}$', '$m_{DM}$', '$g_{DM}$', '$g_{q}$',
        'Data-takingperiod', 'Fullsample', 'Triggeremulation',
        '$p_{T}^{miss}>250$GeV', '$p_{T}^{miss}$qualityfilters', 'Electronveto',
        'Muonveto', 'Tauveto', 'Bjetveto', 'Photonveto',
        '$\Delta \phi (jet,p_{T}^{miss})>0.5$ rad',
        '$\Delta p_{T}^{miss}$ (PF-Cal)$<0.5$ rad',
        'LeadingAK4jet$p_{T}>100$GeV', 'LeadingAK4jet$\eta<2.4$',
        'LeadingAK4jetenergyfractions', 'Mono-Voverlapremoval',
        'HCALmitigation(jets)', 'HCALmitigation($\phi^{miss}$)',
        '$\Delta \phi (\mathrm{PF}_\mathrm{Charged})<2.0$ rad']
    for column in cmsColumns:
        dataDict[column] = None


    # ## Get Model Parameters
    banner = sorted(glob.glob(os.path.dirname(inputFile)+'/*banner.txt'),key=os.path.getmtime,reverse=True)
    if len(banner) == 0:
        print('Banner not found for %s' %inputFile)
    elif len(banner) > 1:        
        print('\n%i banner files found in %s.' 
            %(len(banner),os.path.dirname(inputFile)))
    banner = banner[0]
    xtree = ET.parse(banner)
    xroot = xtree.getroot()
    genInfo = xroot.find('header').find('MGGenerationInfo').text.strip().split('\n')
    genInfo = [x.replace('#','').strip().split(':') for x in genInfo]
    xsecPBall = [eval(x[1]) for x in genInfo if 'Integrated weight (pb)' in x[0]]
    xsecPBmatched = [eval(x[1]) for x in genInfo if 'Matched Integrated weight (pb)' in x[0]]
    if xsecPBmatched:
        xsecPB = xsecPBmatched[0]
    else:
        xsecPB = xsecPBall[0]

    slha = xroot.find('header').find('slha').text
    pars = pyslha.readSLHA(slha)
    mMed = pars.blocks['MASS'][55]
    mDM = pars.blocks['MASS'][52]
    gVq = pars.blocks['DMINPUTS'][4] # Mediator-quark vector coupling
    gAq = pars.blocks['DMINPUTS'][10] # Mediator-quark axial coupling
    gVx = pars.blocks['DMINPUTS'][2] # Mediator-DM vector coupling
    gAx = pars.blocks['DMINPUTS'][3] # Mediator-DM axial coupling
    print('Cross-section (pb) = %1.3e' %xsecPB)
    print('mMed = %1.2f GeV, mDM = %1.2f GeV, gVq = %1.2f, gAq = %1.2f, gVx = %1.2f, gAx = %1.2f' 
        %(mMed,mDM,gVq,gAq,gVx,gAx))


    # #### Store data
    if gVx != 0:
        dataDict['Coupling'] = 'Vector'
    else:
        dataDict['Coupling'] = 'Axial'
        
    dataDict['Mode'] = 'DM+QCDjets'

    dataDict['$m_{med}$'] = mMed
    dataDict['$m_{DM}$'] = mDM
    if dataDict['Coupling'] == 'Vector':
        dataDict['$g_{DM}$'] = gVx
        dataDict['$g_{q}$'] = gVq
    else:
        dataDict['$g_{DM}$'] = gAx
        dataDict['$g_{q}$'] = gAq

    dataDict['Data-takingperiod'] = 2017


    # # Load events, apply cuts and store relevant info

    # ## Cuts
    ## Trigger efficiency
    triggerEff = 0.9 # Applied to the event weights

    ## jets
    pTj1min = 100.
    pTjmin = 25.
    etamax = 2.4
    ## MET
    minMET = 250.
    ## Electrons
    pTmin_el = 10.
    etamax_el = 2.5
    nMax_el = 0
    ## Photons
    pTmin_a = 15.
    etamax_a = 2.5
    nMax_a = 0
    ## Muons
    pTmin_mu = 10.
    etamax_mu = 2.4
    nMax_mu = 0
    ## Tau jets
    nMax_tau = 0
    ## b jets
    nMax_b = 0


    weights = np.array([])
    met = np.array([])
    totalweight = 0.0
    cutFlow = { 'Fullsample' : 0.,
                'Triggeremulation' : 0.,
            '$p_{T}^{miss}>250$GeV' : 0., 
            'Electronveto' : 0.,
            'Muonveto' : 0., 
            'Tauveto' : 0., 
            'Bjetveto' : 0., 
            'Photonveto' : 0.,
            '$\Delta \phi (jet,p_{T}^{miss})>0.5$ rad' : 0.,
            'LeadingAK4jet$p_{T}>100$GeV' : 0., 
            'LeadingAK4jet$\eta<2.4$' : 0.}


    f = ROOT.TFile(inputFile,'read')
    tree = f.Get("Delphes")
    nevts = tree.GetEntries()
    dataDict['Total MC Events'] = nevts


    progressbar = P.ProgressBar(widgets=["Reading Events", P.Percentage(),
                                P.Bar(marker=P.RotatingMarker()), P.ETA()])
    progressbar.maxval = nevts
    progressbar.start()

    for ievt in range(nevts):    
        
        progressbar.update(ievt)
        tree.GetEntry(ievt)        

        jets = tree.Jet
        weight = tree.Weight.At(1).Weight
        totalweight += weight

        missingET = tree.MissingET.At(0)
    #         missingET = tree.GenMissingET.At(0)  # USE REAL MISSING ET!
        electrons = tree.Electron
        muons = tree.Muon
        photons = tree.Photon

        # Filter electrons:
        electronList = []
        for iel in range(electrons.GetEntries()):
            electron = electrons.At(iel)
            if electron.PT < pTmin_el:
                continue
            if abs(electron.Eta) > etamax_el:
                continue
            electronList.append(electron)

        # Filter muons:
        muonList = []
        for imu in range(muons.GetEntries()):
            muon = muons.At(imu)
            if muon.PT < pTmin_mu:
                continue
            if abs(muon.Eta) > etamax_mu:
                continue
            muonList.append(muon)

        # Filter photons:
        photonList = []
        for ia in range(photons.GetEntries()):
            photon = photons.At(ia)
            if photon.PT < pTmin_a:
                continue
            if abs(photon.Eta) > etamax_a:
                continue
            photonList.append(photon)            

        # Filter jets
        jetList = []
        bjetList = []
        taujetList = []
        for ijet in range(jets.GetEntries()):
            jet = jets.At(ijet)
            if jet.PT < pTjmin:
                continue
            if abs(jet.Eta) > 2.5:
                continue
            if jet.BTag:
                bjetList.append(jet)
            elif jet.TauTag:
                taujetList.append(jet)
            else:
                jetList.append(jet)  
        jetList = sorted(jetList, key = lambda j: j.PT, reverse=True)    

        if len(jetList) > 0:
            deltaPhi = np.abs(jetList[0].Phi-missingET.Phi) 
        else:
            deltaPhi = 0.0
        
        # Apply cut on DM pT to reproduce CMS
        # cut on event generation:
        dmMET = tree.DMMissingET.At(0).MET
        if dmMET < 150.0:
            continue
        
        cutFlow['Fullsample'] += weight

        # Apply cuts:
        ## Apply trigger efficiency
        if np.random.uniform() > triggerEff:
            continue
        cutFlow['Triggeremulation'] += weight
        ## Cut on MET
        if missingET.MET < minMET: continue              
        cutFlow['$p_{T}^{miss}>250$GeV'] += weight
        ## Veto electrons
        if len(electronList) > nMax_el: continue  
        cutFlow['Electronveto'] += weight
        ## Veto muons
        if len(muonList) > nMax_mu: continue  
        cutFlow['Muonveto'] += weight
        ## Veto tau jets
        if len(taujetList) > nMax_tau: continue  
        cutFlow['Tauveto'] += weight
        ## Veto b jets
        if len(bjetList) > nMax_b: continue  
        cutFlow['Bjetveto'] += weight
        ## Veto photons
        if len(photonList) > nMax_a: continue  
        cutFlow['Photonveto'] += weight
        ## Delta Phi cut
        if deltaPhi < 0.5: continue
        cutFlow['$\Delta \phi (jet,p_{T}^{miss})>0.5$ rad'] += weight
        ## Jet cuts
        if len(jetList) < 1 or jetList[0].PT < pTj1min: continue
        cutFlow['LeadingAK4jet$p_{T}>100$GeV'] += weight
        if abs(jetList[0].Eta) > etamax: continue
        cutFlow['LeadingAK4jet$\eta<2.4$'] += weight

        # Store relevant data        
        weights = np.append(weights,weight)
        met = np.append(met,missingET.MET)  
        
    f.Close()

    progressbar.finish()
    # Normalize cutFlow by FullSample:
    totWeightCMS = cutFlow['Fullsample']
    for key,val in cutFlow.items():
        cutFlow[key] = val/totWeightCMS

    # ### Store cut-flow
    dataDict.update(cutFlow)

    # ### Get global info and weight in MET bins
    dataDict['Total xsec (pb)'] = totalweight
    dataDict['Total xsec-pT150 (pb)'] = totWeightCMS
    lumi2017 = 41.5
    dataDict['Luminosity (1/fb)'] = lumi2017

    metBins = [250,  280,  310,  340,  370,  400,  430,  470,  510, 550,  590,  640,  690,  
            740,  790,  840,  900,  960, 1020, 1090, 1160, 1250, 99999]
    binc,binEdges = np.histogram(met,bins=metBins, weights=weights)
    binc2,_ = np.histogram(met,bins=metBins, weights=weights**2)
    for ibin,b in enumerate(binc):
        label = 'bin_%1.1f_%1.1f'%(binEdges[ibin],min(1400.0,binEdges[ibin+1]))    
        dataDict[label] = b*1e3*lumi2017
        dataDict[label+'_ErrorPlus'] = np.sqrt(binc2[ibin])*1e3*lumi2017
        dataDict[label+'_ErrorMinus'] = np.sqrt(binc2[ibin])*1e3*lumi2017


    return dataDict


if __name__ == "__main__":
    
    import argparse    
    ap = argparse.ArgumentParser( description=
            "Run the recasting for CMS-EXO-20-004. Store the cutflow and SR bins in a pickle (Pandas DataFrame) file." )
    ap.add_argument('-f', '--inputFile', required=True,
            help='path to the ROOT event file generated by Delphes.')
    ap.add_argument('-v', '--verbose', default='info',
            help='verbose level (debug, info, warning or error). Default is info')


    t0 = time.time()

    # # Set output file
    args = ap.parse_args()
    inputFile = args.inputFile

    outputFile = inputFile.replace('delphes_events.root','cms_exo_20_004.pcl')


    args = ap.parse_args()
    dataDict = getRecastData(inputFile)
    # Convert dataDict to a list with a single entry
    for key,val in dataDict.items():
        dataDict[key] = [val]

    # #### Create pandas DataFrame
    df = pd.DataFrame.from_dict(dataDict)

    # ### Save DataFrame to pickle file
    print('Saving to',outputFile)
    df.to_pickle(outputFile)

    print("\n\nDone in %3.2f min" %((time.time()-t0)/60.))
