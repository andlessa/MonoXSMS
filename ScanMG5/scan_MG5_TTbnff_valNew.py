
#!/usr/bin/env python3
import subprocess
import os
from pathlib import Path
import time

ncores = 7


BASE_PATH = Path(__file__).resolve().parent
MG5_PATH = BASE_PATH / "../../MG5"
FILE_NAME = BASE_PATH / "TT_bnff_1j_match.txt"
OUTPUT_FOLDER = Path("../Output_MC/TTbnff_1j_match_val")
OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

parameters = {
    "PDF": 247000,
    "ne": 30000,
    "ebeam": 6500,
    "mt1": [356, 361, 365, 370, 376, 365, 371, 375, 380, 390, 400, 361, 365, 370, 375, 380, 385, 390, 400, 375, 380, 383, 386, 389, 395, 399, 410, 420, 390, 395, 397, 400, 406, 410, 416, 420, 430, 401, 405, 410, 416, 420, 425, 440, 450, 410, 421, 430, 439, 450, 431, 435, 450, 461, 470, 456, 461, 470, 480, 485, 490, 487, 491, 500, 502, 516, 520, 531, 535, 540, 546, 550],
    "mn1": [300, 300, 300, 300, 300, 319, 319, 319, 319, 320, 319, 329, 330, 329, 329, 330, 329, 330, 330, 349, 349, 349, 349, 349, 349, 349, 349, 349, 364, 365, 365, 365, 365, 365, 365, 365, 364, 380, 379, 379, 379, 379, 380, 380, 379, 400, 399, 399, 400, 400, 420, 421, 420, 420, 421, 449, 449, 450, 450, 450, 450, 480, 480, 480, 490, 501, 501, 520, 520, 520, 540, 540],
}

#
#

def write_initial_config(f, output_folder, params):
    f.write("import model MSSM_SLHA2-full\n")
    f.write("define j = g u c d s b u~ c~ d~ s~ b~\n")
    f.write("generate p p > t1 t1~ / t2 t2~\n")
    f.write("add process p p > t1 t1~ j / t2 t2~\n")
    f.write(f"output {output_folder}\n")
    f.write(f"launch {output_folder}\n")
    f.write("analysis = OFF\n")
    f.write("shower = Pythia8\n")
    f.write("0\n")
    f.write("/home/yoxara/MonoXSMS/ScanMG5/Cards/SUSY/pythia8_card_1j_match.dat\n")
    f.write("/home/yoxara/MonoXSMS/ScanMG5/Cards/SUSY/param_card_450_443.dat\n")
    f.write("set run_card pdlabel lhapdf\n")
    f.write("set run_card pdlabel lhapdf\n")
    f.write(f"set run_card lhaid {params['PDF']}\n")
    f.write(f"set run_card nevents {params['ne']}\n")
    f.write("set run_card dynamical_scale_choice 2\n")


def append_config(f, mt1, mn1, is_last):
    f.write(f"set param_card msu3 {mt1}\n")
    f.write(f"set param_card Mneu1 {mn1}\n")
    f.write(f"set run_card run_tag {mt1:.0f}_{mn1:.0f}\n")
    f.write(f"set run_card xqcut {mt1 / (4 * 1.2)}\n")
    #
    # Launch unless it's the last combination
    if not is_last:
        f.write("launch\n")
    else:
        # Final launch with interactive mode
        f.write(f"launch {OUTPUT_FOLDER} -i\n")
        f.write("exit\n")

def run_madgraph(file_path: Path):
    start_time = time.time()
    env = os.environ.copy()
    env["OMP_NUM_THREADS"] = str(ncores)
    try:
        subprocess.run(["./bin/mg5_aMC", str(file_path)], cwd=MG5_PATH, env=env, check=True)
        elapsed_time = time.time() - start_time
        print(f"MadGraph execution time: {elapsed_time:.2f} seconds")
    except subprocess.CalledProcessError as e:
        print(f"Error during MadGraph execution: {e}")

def process_run(params):
    with open(FILE_NAME, "w") as f:
        write_initial_config(f, OUTPUT_FOLDER, params)
        num_combinations = min(len(params["mt1"]), len(params["mn1"]))
        
        # Loop through each (mt1, mn1) pair and indicate if it's the last combination
        for i, (mt1, mn1) in enumerate(zip(params["mt1"], params["mn1"])):
            is_last = i == num_combinations - 1
            append_config(f, mt1, mn1, is_last)

    run_madgraph(FILE_NAME)

def main():
    process_run(parameters)

if __name__ == "__main__":
    main()
