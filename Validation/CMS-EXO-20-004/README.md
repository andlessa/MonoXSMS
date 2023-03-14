## Authors: ##
[Andre Lessa](mailto:andre.lessa@ufabc.edu.br)
[Camila Ramos](mailto:ramos.camila@aluno.ufabc.edu.br)

# MonoXSMS

Repository for storing the code and results for studies related to LHC Mono-X searches and simplified models (SMS).


## Event Generation ##

In both models, the events are generated at leading order (LO) using MadGraph_aMC@NLO version 3.4.2, with PYTHIA and Delphes versions integrated in MadGraph, with the DMSIMP model implemented. The entire setup can be installed through this [script](../../installer.sh). While the CMS-EXO-20-004 analysis include a combination of the Mono-V and MonoJet signal regions (SRs), the results obtained here only cover the MonoJet SRs. In this validation we use the MLM matching scheme to combine jets from matrix element calculations with the parton shower. 

In both cases, i.e., involving the spin 1 or the spin 0 mediator, the dark matter (DM) pairs are produced firstly with no additional parton, and secondly with one parton. Then, the events are combined. We perform the generations separately since some of the cuts during event selection cannot be implemented otherwise. Other relevant information about the model, event generation or showering, hadronization processes can be found in the [Cards](../../Cards/) folder.

## Event Selection ##

After the generating the events, we randomly split them into three datasets, representing the 2016, 2017, and 2018 for comparison with the background and observed samples given by the CMS analysis. (failure mitigation hcak 2018).In order to reproduce the CMS event selection, the following cuts were implemented after the event generation:

| Variable 	| 		Selection 	    |
| ------------- | --------------------------------- |
|AK4 jets	| $p_{T} > 20,  |\eta| < 2.4$  |
|AK4 leading jet| $p_{T} < 100$ GeV, $|\eta| < 2.4$ |
|tau-tagged jets| $p_{T} > 18$ GeV, $|\eta| < 2.3$  |
|b-tagged jets	| $p_{T} > 20$ GeV, $|\eta| < 2.4$  |
|missing energy | $p_{T}^{miss} > 250$ GeV	    |
| electron veto | $p_{T} > 10$ GeV, $|\eta| < 2.5$  |
| muon veto     | $p_{T} > 10$ GeV, $|\eta| < 2.4$  |
| photon veto   | $p_{T} > 15$ GeV, $|\eta| < 2.5$  |






## Results ##

The following validation plots can be generated running this [ipython notebook](../../notebooks/plotValidation-Axial.ipynb):


![Alt text](../../notebooks/cms_exo_20_004_axial.png?raw=true "Exclusion curve")

![Alt text](../../notebooks/cms_exo_20_004_axial2.png?raw=true "Upper limit comparison")


 * mLLP = 2 TeV, mDM = 1 GeV, Coupling = Axial
 
  | Cut         | CMS eff.        | Recast eff.| 
  | ----------------------- | ----------------- | ------------- | 
  | $p_{T}^{miss} > 250$ GeV |      0.456      |   0.430    | 
  |       Photon veto       |      0.439      |   0.359    |
  | $\Delta \phi (jet, p_{T}^{miss}) > 0.5$ rad |      0.409      |   0.358    |
  |   HCAL mitigation (jets)     |    0.378      |   0.356    |
  
  * mLLP = 2 TeV, mDM = 1 GeV, Coupling = Vector
 
  | Cut         | CMS eff.        | Recast eff.| 
  | ----------------------- | ----------------- | ------------- | 
  | $p_{T}^{miss} > 250$ GeV |      0.452      |   0.462    | 
  |       Photon veto       |      0.436      |   0.384    |
  | $\Delta \phi (jet, p_{T}^{miss}) > 0.5$ rad |      0.406      |   0.383    |
  |   HCAL mitigation (jets)     |    0.376      |   0.380    |
