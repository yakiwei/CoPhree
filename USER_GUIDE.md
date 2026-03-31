\# User Guide: CoPhy Framework



This guide describes the inputs, outputs, and configuration options for the CoPhy reactive transport modeling framework.



\## 1. Inputs (What you need to provide)

COMSOL Model (`/models/.mph`): Defines the physical domain, mesh, and transport properties (fluid flow, dispersion).

PHREEQC Database (`/database/.dat`): Contains thermodynamic constants for aqueous species, minerals, and exchange sites.

Initial Conditions (`/Results/outcon.txt`): A text file containing the initial concentration distribution (typically exported from COMSOL).



\## 2. Outputs (What the code generates)

`outcon.txt`: The raw concentration data exported from COMSOL after the transport step.

`infile.txt`: The geochemically equilibrated concentrations after the PHREEQC step (converted to mmol/L).

`initcon{timestep}.txt`: A timestamped copy of the results for time-series analysis.



\## 3. Configuration Options

You can modify the simulation behavior by editing the following variables in the scripts:

Chemical Parameters: In `phreeqc\_1.py`, you can adjust `temp` (Temperature), `pH`, and `pe` within the `input\_string2` block.

Exchanger Capacity: The surface site density `X` is defined in the `EXCHANGE` block of the PHREEQC input string.

Timestepping: The total number of coupling iterations is controlled by the `range()` loop in `main\_1.py`.



\## 4. Expected Behavior \& Reproducibility

Running the Demo:When you run `main\_1.py`, the console will log the connection to COMSOL and the progress of the PHREEQC solver. 

Reproduction: The provided `Case1\_first.mph` is a synthetic benchmark for \\Cation Exchange\\. Successfully running this demo reproduces the initialization phase (Step 1) of the results shown in Section 3.1 of the associated paper.

Limitations:This demo is configured for a \\single time-step\\ to ensure rapid verification. For full multi-step breakthrough curves, the user must increase the iteration count in the main loop.

