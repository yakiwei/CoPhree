A fully Python-based, modular and reproducible framework for reactive transport modeling in Soil and Groundwater
ComPhy: Coupled COMSOL-PHREEQC in PythonComPhy is a modular, reproducible Python-based framework designed for fully coupled reactive transport modeling (RTM) in soil and groundwater systems.
By integrating the multiphysics capabilities of COMSOL with the geochemical precision of PHREEQC, this framework allows for automated, bidirectional data exchange at each time-step. Unlike its predecessor, ComPhy is entirely independent of the MATLAB environment, offering a more accessible and streamlined workflow for the scientific community.

🚀 Key FeaturesPython-Native: Complete independence from MATLAB, improving portability and reducing licensing hurdles.
Modular Architecture: Functional components are decoupled, allowing users to easily swap or extend geochemical modules or physical solvers.
Bidirectional Coupling: Seamless data exchange between COMSOL (physics/transport) and PHREEQC (chemistry) at the time-step scale.
Validated Accuracy: Proven numerical consistency against benchmark cases (Cation Exchange and Pesticide Transport).
Reproducible Research: Designed with an emphasis on open-source accessibility and automated workflows.

🛠 ArchitectureThe framework is built on a modular design to ensure that the physical simulation and chemical reaction components can be maintained and updated independently.
Transport Engine: Handles spatial discretization and fluid flow (COMSOL Multiphysics).
Chemical Engine: Manages complex aqueous speciation and mineral kinetics (PHREEQC).
Interface Layer: Python-based automation that synchronizes time-stepping and data mapping.

📂 Project Structure (Required for Reproducibility)To ensure the scripts can locate files using relative paths, please organize your local directory as follows:
plaintext
ComPhy_Project/
├── main_1.py              # Initialization runner (Calls comsol_1 & phreeqc_1)
├── comsol_1.py            # Physics initialization script
├── phreeqc_1.py           # Chemical equilibrium initialization script
├── models/                # Directory for COMSOL models
│   └── Case1_first.mph    # Initialization .mph file
├── database/              # Directory for PHREEQC databases
│   └── phreeqc.dat        # PHREEQC database file
├── Results/               # Directory for automated data exchange (txt/csv)
└── README.md

📋 Prerequisites
To run ComPhy, you will need:
Python 3.8+
COMSOL Multiphysics 6.0+ (with MPH interface/API enabled)
RAM: 16 GB recommended.
CPU: 4 cores or more.
Operating System: Windows 10/11 (required for COMSOL-Python MPH interface).
Required Python packages:numpy, mph (for COMSOL-Python bridging),phreeqc (Python interface for IPhreeqc)

Python Dependencies
bash
pip install numpy mph phreeqpc

🏁 Quick Start: Runnable Example (Single-Step)
This repository includes a pre-configured test case to verify your environment. The scripts use relative paths and will automatically redirect COMSOL's export path to the local /Results folder.
Start COMSOL Server: Open the "COMSOL Multiphysics Server" application on your computer.
Prepare Files: Ensure Case1_first.mph is in the models/ folder and phreeqc.dat is in the database/ folder.
Run the Test:
bash
python main_1.py
Verification: Upon completion (~2 minutes), check the Results/ folder. You should see outcon.txt and infile.txt. Compare these with any provided expected results to confirm success.

📖 Tutorial for Typical Use Cases
This section provides a step-by-step guide for standard coupled reactive transport simulations.
Set up or load a COMSOL model (.mph) with flow and solute transport physics.
Configure initial and boundary conditions in the COMSOL model.
Prepare geochemical conditions in phreeqc_1.py and select the appropriate database.
Launch the COMSOL Server to enable Python-COMSOL communication.
Run the main script to start the fully coupled simulation.
The framework automatically exchanges concentration fields between COMSOL and PHREEQC at each time step.
View output files in the Results/ folder for post-processing and plotting.

📘 User Guide
Inputs
COMSOL model file (.mph) in the models/ folder
PHREEQC database file (.dat) in the database/ folder
Initial and boundary conditions defined in COMSOL or Python scripts
Outputs
infile.txt: Physical concentration data sent from COMSOL to PHREEQC
outcon.txt: Geochemical results returned to COMSOL
Time-step results and intermediate files saved in the Results/ directory
Options & Modifications
Adjust time stepping in comsol_1.py
Modify geochemical reactions and species in phreeqc_1.py
Change mesh, flow parameters, and boundary conditions directly in COMSOL
Add or remove geochemical modules via the modular interface
Expected Behavior
The program runs automatically in a loop: COMSOL transport → PHREEQC reaction → update fields
No manual intervention is needed during simulation
All intermediate files are written to the Results/ folder
Simulation duration depends on model resolution, CPU, and RAM

🔬 Reproducing the Main Results in the Paper
This repository provides all code, model structures, and workflows required to reproduce the benchmark results presented in the associated paper, including:
Cation Exchange benchmark
Pesticide reactive transport benchmark
To reproduce the main results:
Use the provided COMSOL model Case1_first.mph
Use the default PHREEQC database phreeqc.dat
Run main_1.py
The output files in Results/ can be used to generate figures and tables consistent with the publication.
If real field or experimental data cannot be shared due to size or privacy restrictions, a synthetic dataset or simplified dummy model is provided to ensure full testability of the coupling workflow.

📌 Security & File Format Note
For security reasons, this repository does not use or accept single compressed files (e.g., .zip, .rar, .7z).All code, models, scripts, and examples are provided as individual, directly accessible files.

License: This project is licensed under the MIT License.

📧 Contact
Proposed by Yaqiang Wei, Jiao Zhang in 2026Contact: yakiwei@yahoo.com
