#!/usr/bin/env python3
# chmod +x runScanMA5expert.py
# ./runScanMA5expert.py -p scan_DMA.ini

import pexpect
import os
import sys
import glob
from confParser import parse_config, parse_arguments
import shutil
import re

def main(config_file):
    # Parse the configuration file
    config = parse_config(config_file)
    
    # Extract paths and configurations from the configuration file
    ma5_path = config['MadAnalysis5']['ma5_path']
    card_path = config['MadAnalysis5']['card_path']
    global_likelihoods = config['MadAnalysis5']['global_likelihoods']
    store_root = config['MadAnalysis5']['store_root']
    recast = config['MadAnalysis5']['recast']
    pattern = config['EventFiles']['pattern']
    analysis_name = config['Analysis']['analysis_name']
    label = config['Analysis']['label']

    # Use dictionary `get` method to retrieve optional parameters, defaulting to None if not present
    x_section = config['Analysis'].get('value_Xsection')
    integrated_Luminosity = config['Analysis'].get('value_integrated_Luminosity')
    value_systematics = config['Analysis'].get('systematics')
    value_systematics2 = config['Analysis'].get('systematics2')
    scale_up_variation = config['Analysis'].get('scale_up_variation')
    scale_down_variation = config['Analysis'].get('scale_down_variation')
    pdf_up_variation = config['Analysis'].get('pdf_up_variation')
    pdf_down_variation = config['Analysis'].get('pdf_down_variation')

    # Find all event files matching the pattern
    event_files = sorted(glob.glob(pattern))
    print(f"Found {len(event_files)} files matching the pattern.")

    for i, filepath in enumerate(event_files):
        print(f"Processing file: {filepath}")
        match = re.search(r'run_(\d+)', filepath)
        run_number = match.group(1) if match else "unknown"
        print(f"Run number: {run_number}")

        filename = os.path.basename(filepath)
        parts = filename.split('_')  
        unique_identifier = '_'.join(parts[:-2]).replace('.', '_')
        specific__dataset_label = f"{label}_run_{run_number}_{unique_identifier}"
        specific_analysis_name = f"{analysis_name}_run_{run_number}_{unique_identifier}"

        procCard = "recast_script.txt"
        try:
            with open(procCard, 'w') as script_file:
                # Remove existing directories if they exist
                for dir_suffix in ["", "_SFSRun"]:
                    dir_path = specific_analysis_name + dir_suffix
                    if os.path.exists(dir_path):
                        shutil.rmtree(dir_path)
                        print(f"Removed existing directory: {dir_path}")

                # Write recast settings to the script
                script_file.write(f"set main.recast = {recast}\n")
                script_file.write(f"set main.recast.store_root = {store_root}\n")
                script_file.write(f'set main.recast.global_likelihoods = {global_likelihoods}\n')
                script_file.write(f"import {filepath} as {specific__dataset_label}\n")
                script_file.write(f"set main.recast.card_path = {card_path}\n")
                
                # Write optional settings if they are present
                if x_section:
                    print(f"x_section: {x_section}")
                    script_file.write(f"set {specific__dataset_label}.xsection = {x_section}\n")
                
                if integrated_Luminosity:
                    print(f"integrated_Luminosity: {integrated_Luminosity}")
                    script_file.write(f"set main.recast.add.extrapolated_luminosity = {integrated_Luminosity}\n")
                
                if value_systematics:
                    print(f"value_systematics: {value_systematics}")
                    script_file.write(f"set main.recast.add.systematics = {value_systematics}\n")

                if value_systematics2:
                    print(f"value_systematics2: {value_systematics2}")
                    script_file.write(f"set main.recast.add.systematics = {value_systematics2}\n")

                # Write scale and PDF variations using a loop
                for variation, name in [(scale_up_variation, "scale_up_variation"),
                                        (scale_down_variation, "scale_down_variation"),
                                        (pdf_up_variation, "pdf_up_variation"),
                                        (pdf_down_variation, "pdf_down_variation")]:
                    if variation:
                        print(f"{name}: {variation}")
                        script_file.write(f"set {specific__dataset_label}.{name} = {variation}\n")
                
                script_file.write(f"submit {specific_analysis_name}\n")

        except IOError as e:
            print(f"Error writing to {procCard}: {e}")
            continue

        # Command to execute MA5
        full_command = f'{ma5_path}/bin/ma5 -R {procCard}'
        try:
            with pexpect.spawn(full_command, timeout=None, encoding='utf-8') as child:
                child.logfile = sys.stdout

                # Wait for and respond to known questions
                try:
                    index = child.expect(["Answer:"], timeout=None)
                    if index == 0:
                        child.sendline("N")
                except pexpect.EOF:
                    pass

                child.sendline("exit")
                child.expect(pexpect.EOF, timeout=None)

        except pexpect.ExceptionPexpect as e:
            print(f"Error executing MA5: {e}")
            continue

        # Remove the procCard after each run
        try:
            os.remove(procCard)
        except OSError as e:
            print(f"Error removing {procCard}: {e}")

if __name__ == "__main__":
    config_path = parse_arguments()
    main(config_path)
