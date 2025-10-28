#!/usr/bin/env python3

import os, re, glob
import pandas as pd
import pylhe
import pyslha
import numpy as np
import xml.etree.ElementTree as ET

# SAF and CLs file patterns
cutflow_patterns = ['/home/ramos/madanalysis5-1_11_0/ANALYSIS_17/Output/SAF/dmp_1_350_1j_match/atlas_exot_2018_06/Cutflows/*.saf']
saf_patterns = ['/home/ramos/madanalysis5-1_11_0/ANALYSIS_17/Output/SAF/*/*.saf']
cls_patterns = ['/home/ramos/madanalysis5-1_11_0/ANALYSIS_17/Output/SAF/*/CLs_output.dat']
inputList_pattern = sorted(glob.glob('/home/ramos/madanalysis5-1_11_0/ANALYSIS_17/Input/*.list'))

saf_to_theoretical = {}
final_results = []
allDataDicts = []

cutflow_files = sorted([file for pattern in cutflow_patterns for file in glob.glob(pattern)])
saf_files = sorted([file for pattern in saf_patterns for file in glob.glob(pattern)])
cls_files = sorted([file for pattern in cls_patterns for file in glob.glob(pattern)])


if len(inputList_pattern) != len(cls_files):
    print(f"Warning: Mismatch in input files ({len(inputList_pattern)}) and CLs files ({len(cls_files)})!")

sample_global_info_pattern = re.compile(r"<SampleGlobalInfo>(.*?)</SampleGlobalInfo>", re.DOTALL)

# Process SAF and CLs files in pairs
for inputFile, cls_file, saf_file in zip(inputList_pattern, cls_files, saf_files):
    try:
        # Read the HepMC file location from the input file
        with open(inputFile, 'r') as f:
            hepMCfile = f.read().strip()

        hepMCfile_list = hepMCfile.split('\n')
        if not hepMCfile_list:
            print(f"Cannot obtain banner, no hepmc file in Input.")
            continue

        
        hepDir = os.path.dirname(hepMCfile_list[0])
        print(hepDir)
        banner_candidates = glob.glob(f"{hepDir}/**/*banner.txt", recursive=True)
        
        if not banner_candidates:
            print(f"No banner file found for input file: {inputFile}")
            continue
        
        # Use the most recently modified banner file
        banner_file = max(banner_candidates, key=os.path.getmtime)

        # SLHA information from the banner file
        xtree = ET.parse(banner_file)
        xroot = xtree.getroot()
        slha = xroot.find('header').find('slha').text
        pars = pyslha.readSLHA(slha)
        mMed = pars.blocks['MASS'].get(55)  # mediator mass
        mchi = pars.blocks['MASS'].get(52)  # DM mass

        if mMed is None or mchi is None:
            print(f"Masses not found in SLHA block for {inputFile}")
            continue

        allDataDicts.append({
            "Input File": inputFile,
            "CLs File": cls_file,
            "SAF File": saf_file,
            "HepMC Dir": hepDir,
            "Banner File": banner_file,
            "mMed (GeV)": mMed,
            "mchi (GeV)": mchi
        })

        # theoretical cross-section from the SAF file
        sigma_theoretical = None
        with open(saf_file, 'r') as file:
            content = file.read()
            match = sample_global_info_pattern.search(content)
            if match:
                block_content = match.group(1).strip()
                for line in block_content.splitlines():
                    line = line.strip()
                    if line and not line.startswith("#"):
                        try:
                            sigma_theoretical = float(line.split()[0])
                            saf_to_theoretical[os.path.basename(saf_file).replace('.saf', '')] = sigma_theoretical
                            break  
                        except ValueError:
                            pass
        if sigma_theoretical is None:
            print(f"Could not extract cross-section from SAF file: {saf_file}")
            continue

        # Process the CLs_output.dat file
        with open(cls_file.strip(), 'r') as f:
            lines_output = f.readlines()

        for line in lines_output:
            if not line.strip():  
                continue
            if not line.strip().startswith("#"): 
                if "||" not in line:
                    print(f"Skipping malformed line: {line.strip()}")
                    continue
                try:
                    main_part, efficiency_part = line.split("||")
                    main_parts = re.split(r'\s{2,}', main_part.strip())
                    efficiency_parts = re.split(r'\s+', efficiency_part.strip())

                    if len(main_parts) < 4 or len(efficiency_parts) < 2:
                        print(f"Incomplete line detected: {line.strip()}")
                        continue
                    # print(main_parts)

                    sr = main_parts[1]  # Signal region
                    sigma_exp = float(main_parts[3])  # Sigma_95_exp
                    sigma_obs = float(main_parts[4].split('.')[0] + '.' + main_parts[4].split('.')[1][:-1])  # Sigma_95_obs
                    # efficiency = float(efficiency_parts[0])  # Efficiency
                    # stat = float(efficiency_parts[1])  # Statistical uncertainty
                    final_results.append((sr, sigma_exp, sigma_obs,
                                          sigma_theoretical, os.path.basename(saf_file).replace('.saf', ''),
                                          mMed, mchi))
                except (ValueError, IndexError) as e:
                    print(f"Error processing line: {line.strip()}\n{e}")

    except FileNotFoundError as e:
        print(f"File not found error for {inputFile}: {e}")
    except ET.ParseError as e:
        print(f"Error parsing XML in {banner_file}: {e}")
    except Exception as e:
        print(f"Unexpected error processing {inputFile}: {e}")

df_data = pd.DataFrame(allDataDicts)

df_final_results = pd.DataFrame(
    final_results,
     columns=["Signal Region", "Sigma_95_exp (pb)", "Sigma_95_obs (pb)",
             "Sigma_theoretical (pb)", "SAF File", "mMed (GeV)", "mchi (GeV)"])

# Get efficiencies and error

def extract_all_cuts_weights(em_file_path):
    with open(em_file_path, 'r') as file:
        lines = file.readlines()
    weights = {}
    weights_sq = {}
    for i, line in enumerate(lines):
        if line.startswith('<Counter>') or line.startswith('<InitialCounter>'):
            cut_name = lines[i + 1].strip().split('"')[1]
            if 'sum of weights' and not '^2' in lines[i + 2]:
                val = float(lines[i + 3].split()[0])
                valsq = float(lines[i + 4].split()[0])
                weights[cut_name] = val
                weights_sq[cut_name] = valsq
    return weights, weights_sq

# Define the desired cuts
desired_cuts = [
    'Initial number of events','MET > 200 GeV(IM0)', 'MET > 250 GeV(IM1)', 
    'MET > 300 GeV(IM2)', 'MET > 350 GeV(IM3)', 'MET > 400 GeV(IM4)', 
    'MET > 500 GeV(IM5)', 'MET > 600 GeV(IM6)', 'MET > 700 GeV(IM7)', 
    'MET > 800 GeV(IM8)', 'MET > 900 GeV(IM9)', 'MET > 1000 GeV(IM10)', 
    'MET > 1100 GeV(IM11)', 'MET > 1200 GeV(IM12)','200 < MET < 250 GeV', 
    '250 < MET < 300 GeV', '300 < MET < 350 GeV', '350 < MET < 400 GeV', 
    '400 < MET < 500 GeV', '500 < MET < 600 GeV', '600 < MET < 700 GeV', 
    '700 < MET < 800 GeV', '800 < MET < 900 GeV', '900 < MET < 1000 GeV', 
    '1000 < MET < 1100 GeV', '1100 < MET < 1200 GeV', 'MET < 1200 GeV'
]


# Notify if no files were found for the current base path
if not cutflow_files:
    print(f"No input files found for base path: {cutflow_patterns}")
   

w_dict, w2_dict = {}, {}

for em_file in cutflow_files:
    w_dict[em_file], w2_dict[em_file] = extract_all_cuts_weights(em_file)


# Create the nentries array with relevant cuts
weights = [0] * len(desired_cuts)
weights_sq = [0] * len(desired_cuts)

for cuts in w_dict.values():
    for i, cut in enumerate(desired_cuts):
        if cut in cuts:
            weights[i] = cuts[cut]

for cuts in w2_dict.values():
    for i, cut in enumerate(desired_cuts):
        if cut in cuts:
            weights_sq[i] = cuts[cut]


n_err = np.sqrt(np.array(weights_sq[1:]))
n_tot = weights[0]
effs = np.array(weights[1:])/n_tot
# effErr = (nerr / nevts) * eff
effs_stat = (n_err / n_tot) * effs

df_final_results['Efficiency'] = effs
df_final_results['Efficiency_Err'] = effs_stat


df_final_results.to_pickle('/home/ramos/MonoXSMS-camila/ATLAS-EXOT-2018-06/ma5_test_spin1/ma5Results_axial.pcl')