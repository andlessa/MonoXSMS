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
def getRecastData(inputFiles):

    if len(inputFiles) == 1:
        modelDict = {'filename' : os.path.abspath(inputFiles[0])}
    else:
        modelDict = {'filename' : os.path.abspath(inputFiles[0])+"+"}
        print('Combining files:')
        for f in inputFiles:
            print(f)

    cmsColumns = ['Coupling', 'Mode', '$m_{med}$', '$m_{DM}$', '$g_{DM}$', '$g_{q}$']
    
    for column in cmsColumns:
        modelDict[column] = None
    
    # ## Get Model Parameters
    banner = sorted(glob.glob(os.path.dirname(inputFiles[0])+'/*banner.txt'),key=os.path.getmtime,reverse=True)
    if len(banner) == 0:
        print('Banner not found for %s' %inputFiles[0])
    elif len(banner) > 1:        
        print('\n%i banner files found in %s.' 
            %(len(banner),os.path.dirname(inputFiles[0])))
    banner = banner[0]
    xtree = ET.parse(banner)
    xroot = xtree.getroot()
    # genInfo = xroot.find('header').find('MGGenerationInfo').text.strip().split('\n')
    # genInfo = [x.replace('#','').strip().split(':') for x in genInfo]
    # xsecPBall = [eval(x[1]) for x in genInfo if 'Integrated weight (pb)' in x[0]]
    # xsecPBmatched = [eval(x[1]) for x in genInfo if 'Matched Integrated weight (pb)' in x[0]]
    # if xsecPBmatched:
    #     xsecPB = xsecPBmatched[0]
    # else:
    #     xsecPB = xsecPBall[0]

    slha = xroot.find('header').find('slha').text
    pars = pyslha.readSLHA(slha)
    mMed = pars.blocks['MASS'][55]
    mDM = pars.blocks['MASS'][52]
    gVq = pars.blocks['DMINPUTS'][4] # Mediator-quark vector coupling
    gAq = pars.blocks['DMINPUTS'][10] # Mediator-quark axial coupling
    gVx = pars.blocks['DMINPUTS'][2] # Mediator-DM vector coupling
    gAx = pars.blocks['DMINPUTS'][3] # Mediator-DM axial coupling
    print('\nModel parameters:')
    print('mMed = %1.2f GeV, mDM = %1.2f GeV, gVq = %1.2f, gAq = %1.2f, gVx = %1.2f, gAx = %1.2f\n' 
        %(mMed,mDM,gVq,gAq,gVx,gAx))


    # #### Store data
    if gVx != 0:
        modelDict['Coupling'] = 'Vector'
    else:
        modelDict['Coupling'] = 'Axial'
        
    modelDict['Mode'] = 'DM+QCDjets'

    modelDict['$m_{med}$'] = mMed
    modelDict['$m_{DM}$'] = mDM
    if modelDict['Coupling'] == 'Vector':
        modelDict['$g_{DM}$'] = gVx
        modelDict['$g_{q}$'] = gVq
    else:
        modelDict['$g_{DM}$'] = gAx
        modelDict['$g_{q}$'] = gAq

    
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

    def passVetoJets2018(jets):
        """
        Calorimeter mitigation failure I for the 2018
        data set.

        :param jets: List of Jet objects

        :return: True if event should be accepted, False otherwise.
        """

        for jet in jets:
            if jet.PT < 30.0:
                continue
            if jet.Phi < -1.57 or jet.Phi > -0.87:
                continue
            if jet.Eta < -3.0 or jet.Eta > -1.3:
                continue
            return False
        return True

    def passVetoPtMiss2018(met):
        """
        Calorimeter mitigation failure II for the 2018
        data set.

        :param met: MET object

        :return: True if event should be accepted, False otherwise.
        """        

        if met.MET > 470.:
            return True
        if met.Phi < -1.62 or met.Phi > -0.62:
            return True
        return False

    weights = []
    met = []
    totalweight = 0.0
    # Keep track of two weights 
    # (one for the 2016-2017 datasets and one for 2018)
    zeroWeight = np.zeros(2)
    cutFlow = { 'Fullsample' : zeroWeight.copy(),
                'Triggeremulation' : zeroWeight.copy(),
            '$p_{T}^{miss}>250$GeV' : zeroWeight.copy(), 
            'Electronveto' : zeroWeight.copy(),
            'Muonveto' : zeroWeight.copy(), 
            'Tauveto' : zeroWeight.copy(), 
            'Bjetveto' : zeroWeight.copy(), 
            'Photonveto' : zeroWeight.copy(),
            '$\Delta \phi (jet,p_{T}^{miss})>0.5$ rad' : zeroWeight.copy(),
            'LeadingAK4jet$p_{T}>100$GeV' : zeroWeight.copy(), 
            'LeadingAK4jet$\eta<2.4$' : zeroWeight.copy(),            
            'HCALmitigation(jets)' : zeroWeight.copy(),
            'HCALmitigation($\phi^{miss}$)' : zeroWeight.copy()
            }

    modelDict['Total MC Events'] = 0
    for inputFile in inputFiles:
        f = ROOT.TFile(inputFile,'read')
        tree = f.Get("Delphes")
        nevts = tree.GetEntries()
        modelDict['Total MC Events'] += nevts


        progressbar = P.ProgressBar(widgets=["Reading %i Events: " %nevts, P.Percentage(),
                                    P.Bar(marker=P.RotatingMarker()), P.ETA()])
        progressbar.maxval = nevts
        progressbar.start()

        for ievt in range(nevts):    
            
            progressbar.update(ievt)
            tree.GetEntry(ievt)        

            jets = tree.Jet
            weight = np.full(2,tree.Weight.At(1).Weight)
            totalweight += tree.Weight.At(1).Weight

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
            weight = weight*triggerEff
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
            ## 2018 Calorimeter mitigation cuts:
            ### Jet cut:
            if not passVetoJets2018(jetList):
                weight[1] = 0.0 # Zero weight for 2018 dataset
            cutFlow['HCALmitigation(jets)'] += weight
            if not passVetoPtMiss2018(missingET):
                weight[1] = 0.0 # Zero weight for 2018 dataset
            cutFlow['HCALmitigation($\phi^{miss}$)'] += weight

            # Store relevant data        
            weights.append(weight)
            met.append(missingET.MET)  
            
        f.Close()
        progressbar.finish()

    weights = np.array(weights)

    # Normalize cutFlow by FullSample:
    totWeightCMS = cutFlow['Fullsample'][0]
    for key,val in cutFlow.items():
        cutFlow[key] = val/totWeightCMS
    modelDict['Total xsec (pb)'] = totalweight
    modelDict['Total xsec-pT150 (pb)'] = totWeightCMS

    metBins = [250,  280,  310,  340,  370,  400,  430,  470,  510, 550,  590,  640,  690,  
            740,  790,  840,  900,  960, 1020, 1090, 1160, 1250, 99999]

    # Create a dictionary with lists for each datasets
    dataDict = {'Data-takingperiod' : [2016,2017,2018]}
    dataDict.update({'Luminosity (1/fb)' : [36.0,41.5,59.7]})
    for ibin,b in enumerate(metBins[:-1]):
        label = 'bin_%1.1f_%1.1f'%(b,min(1400.0,metBins[ibin+1]))
        dataDict[label] = []
        dataDict[label+'_ErrorPlus'] = []
        dataDict[label+'_ErrorMinus'] = []

    # Split results into 3 data taking periods:
    dataDict.update({key : [] for key in modelDict})
    dataDict.update({key : [] for key in cutFlow})

    for idp,dp in enumerate(dataDict['Data-takingperiod']):
        lumi = dataDict['Luminosity (1/fb)'][idp]
        # Store common values to all datasets:
        for key,val in modelDict.items():
            dataDict[key].append(val)
        # Store dataset-dependent cutflows:
        for key,val in cutFlow.items():
            if dp == 2018:
                w = val[1] # Use weight with mitigation
            else:
                w = val[0]
            dataDict[key].append(w)
        # Store MET bins:
        if dp == 2018:
            w = weights[:,1] # Use weight with mitigation
        else:
            w = weights[:,0]
        binc,binEdges = np.histogram(met,bins=metBins, weights=w)
        binc2,_ = np.histogram(met,bins=metBins, weights=w**2)
        for ibin,b in enumerate(binc):
            label = 'bin_%1.1f_%1.1f'%(binEdges[ibin],min(1400.0,binEdges[ibin+1]))    
            dataDict[label].append(b*1e3*lumi)
            dataDict[label+'_ErrorPlus'].append(np.sqrt(binc2[ibin])*1e3*lumi)
            dataDict[label+'_ErrorMinus'].append(np.sqrt(binc2[ibin])*1e3*lumi)

    return dataDict


if __name__ == "__main__":
    
    import argparse    
    ap = argparse.ArgumentParser( description=
            "Run the recasting for CMS-EXO-20-004 using one or multiple Delphes ROOT files as input. "
            + "If multiple files are given as argument, combine them. "
            + " Store the cutflow and SR bins in a pickle (Pandas DataFrame) file." )
    ap.add_argument('-f', '--inputFile', required=True,nargs='+',
            help='path to the ROOT event file(s) generated by Delphes.', default =[])
    ap.add_argument('-o', '--outputFile', required=False,
            help='path to output file storing the DataFrame with the recasting data.'
                 + 'If not defined, will use the name of the first input file', 
            default = None)

    ap.add_argument('-v', '--verbose', default='info',
            help='verbose level (debug, info, warning or error). Default is info')


    t0 = time.time()

    # # Set output file
    args = ap.parse_args()
    inputFiles = args.inputFile
    outputFile = args.outputFile
    if outputFile is None:
        outputFile = inputFiles[0].replace('delphes_events.root','cms_exo_20_004.pcl')

    if os.path.splitext(outputFile)[1] != '.pcl':
        outputFile = os.path.splitext(outputFile)[0] + '.pcl'

    modelDict = getRecastData(inputFiles)

    # #### Create pandas DataFrame
    df = pd.DataFrame.from_dict(modelDict)

    # ### Save DataFrame to pickle file
    print('Saving to',outputFile)
    df.to_pickle(outputFile)

    print("\n\nDone in %3.2f min" %((time.time()-t0)/60.))
