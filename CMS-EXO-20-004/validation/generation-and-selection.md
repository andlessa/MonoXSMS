## Event Generation ##

In both models, the events are generated at leading order (LO) using MadGraph_aMC@NLO version 3.4.2, with PYTHIA and Delphes versions integrated within MadGraph, and with the DMSIMP model implemented. The entire setup can be installed through this [script](../../installer.sh). While the CMS-EXO-20-004 analysis include a combination of the Mono-V and MonoJet signal regions (SRs), the results obtained here only cover the MonoJet SRs.

The DM pairs are produced firstly with no additional parton, and secondly with one parton. During the generation a bias module is used on the jet transverse momentum ($p_{T}$) in order to smoothen the event distributions. Additionally, we use the MLM matching scheme to combine jets from matrix element calculatrions with the parton shower. Then, the events are combined. We perform the generations separately since the bias module cannot be implemented with the MLM matching scheme otherwise. It is also important to mention that we do not perform event generations with two additional partons, as done by the CMS-EXO-20-004 analysis in some events for the spin-1 mediators cases.

For the showering process we vary the cutoff scale "xqcut", depending on whether the production is on-shell or not. If the process is on-shell, then the xqcut value is set as $m_{med}/15$ ($m_{med}/12$ for the model with a scalar mediator). On the other hand, if the process is off-shell, then the xqcut value is set as $2m_{\chi}/15$ ($2m_{\chi}/12$). In the case of both particles being too light, we choose xqcut = $30$ GeV.

Other relevant information about the model, event generation or showering and hadronization processes can be found in the [Cards](../../Cards/) folder.

## Event Selection ##

After generating the events, we randomly split them into three datasets, representing the 2016, 2017, and 2018 data for comparison with the background and observed samples given by the CMS analysis. For the 2018 dataset, due to a failure in a section of the calorimeter, a specific selection was applied in the CMS analysis in order to avoid contamination from the mismeasument in the data taking period. We implement the same veto for the specific dataset, as shown in the table below. Therefore, in order to reproduce the CMS event selection, the other following cuts were applied after the event generation:

| Variable 	  | 		Selection		|
| :------------- | :---------------------------------: |
| Trigger emulation | $p_{T}^{miss} > 120$ GeV         |
|AK4 jets	| $p_{T} > 20$ GeV,  $\|\eta\| < 2.4$  |
|AK4 leading jet| $p_{T} < 100$ GeV, $\|\eta\| < 2.4$ |
|tau-tagged jets| $n_{j}^{max} = 0$ ($p_{T} > 18$ GeV, $\|\eta\| < 2.3$)  |
|b-tagged jets	| $n_{j}^{max} = 0$ ($p_{T} > 20$ GeV, $\|\eta\| < 2.4$)  |
|missing energy | $p_{T}^{miss} > 250$ GeV	    |
| electron veto | $n_{j}^{max} = 0$ ($p_{T} > 10$ GeV, $\|\eta\| < 2.5$)  |
| muon veto     | $n_{j}^{max} = 0$ ($p_{T} > 10$ GeV, $\|\eta\| < 2.4$)  |
| photon veto   | $n_{j}^{max} = 0$ ($p_{T} > 15$ GeV, $\|\eta\| < 2.5$)  |
|HCAL failure mitigation (2018) | no AK4 jet with $p_{T} > 30$ GeV, $-1.57 < \phi < -0.87$ rad, and $-3.0 < \eta < -1.3$ rad |
|HCAL failure mitigation (2018) | $p_{T}^{miss} < 470$ GeV with $-1.62 < \phi(p_{T}^{miss}) < -0.62$ rad|
| artificial $p_{T}^{miss}$ mitigation | $\Delta \phi (p_{T}^{jet}, p_{T}^{miss}) > 0.5$ rad |

Note that $n_{j}^{max}$ is the maximum number of jets. 
It is important to emphasize that the table above does not contain all of the cuts employed by the CMS analysis, only the ones we are able to reproduce. Some of the additional selection criteria can be found in the table below.

|               Variable         |              Selection              |
| :----------------------------- | :---------------------------------: |
| PF reconstruction failure mitigation ($p_{T}^{miss}$) | $\Delta p_{T}^{miss} (\mathrm{PF}-\mathrm{Cal}) < 0.5$ |
| PF reconstruction failure mitigation ($\phi$) | $\Delta \phi(\mathrm{PF}_{\mathrm{charged}}) < 2.0$ rad |
| Mono-V removal | ----- |
| $p_{T}^{miss}$ quality filters | ----- |
| Leading AK4 jet  energy fractions | ----- |


The Mono-V overlap removal is not considered since we only generated are Monojet events. For the remaining selection variables, the $p_{T}^{miss}$ quality filters and Leading AK4 jet  energy fractions involve a multiple set of benchmarks described here (ref). 

The event selection is implemented through this [python script](../../cms_exo_20_004-Recast.py), using the root file output from the event generation. This [README](../../README.md) card describes step by step how to generate events, apply the necessary cuts, combine the data and finally estimate the upper limit on the signal events. When perfoming the event selection, we apply the cut $p_{T} > 150$ GeV for the spin-1 mediator case only. The same selection was made on the CMS analysis, however this occurs during event generation. 


