import os
import shutil
from comsol_1 import comsol_first_step
from phreeqc_1 import phreeqc_first_step


def main_1():
    # Set up base directory relative to this script
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    results_dir = os.path.join(BASE_DIR, 'Results')

    # Path to the first initialization model in the 'models' folder
    mph_file = os.path.join(BASE_DIR, 'models', 'Case1_first.mph')

    # 1. Run COMSOL initialization
    comsol_first_step(mph_file)

    # 2. Handle data exchange
    comsol_outcon_path = os.path.join(results_dir, "outcon.txt")
    outcon_copy_path = os.path.join(results_dir, "outcon720.txt")

    if os.path.exists(comsol_outcon_path):
        shutil.copy(comsol_outcon_path, outcon_copy_path)
    else:
        raise FileNotFoundError(f"COMSOL export failed: {comsol_outcon_path} not found.")

    # 3. Run PHREEQC chemical equilibrium
    phreeqc_first_step()


if __name__ == "__main__":
    main_1()