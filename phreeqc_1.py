import numpy as np
import os
from phreeqc import Phreeqc


def phreeqc_first_step():
    # Set up relative paths
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, 'database', 'phreeqc.dat')
    results_dir = os.path.join(BASE_DIR, 'Results')

    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    def selected_array(database, input_string):
        p = Phreeqc()
        p.set_output_string_on(True)
        if p.load_database(database) != 0:
            raise RuntimeError(f"Failed to load database: {database}")
        if p.run_string(input_string) != 0:
            raise RuntimeError("Failed to run PHREEQC input string")
        return p.get_selected_output()

    # Load COMSOL output
    infile_path = os.path.join(results_dir, 'outcon.txt')
    if not os.path.exists(infile_path):
        raise FileNotFoundError(f"Input file not found: {infile_path}")

    infile = np.loadtxt(infile_path, comments='%', delimiter=None)
    m, cols = infile.shape
    n = cols - 1
    outn = 6
    phresult = np.zeros((m, outn))

    # Construct PHREEQC input string
    input_string_all = ""
    for i in range(m):
        # Handle negative concentrations
        for j in range(1, 5):
            if infile[i, j] < 0:
                infile[i, j] = 0

        input_block = f"""
        SOLUTION {i + 1}
            units            mmol/kgw 
            temp             25.0 
            pH               7.0     charge 
            pe               12.5    O2(g)   -0.68 
            Ca               {round(infile[i, 1], 15)}
            Cl               {round(infile[i, 2], 10)}
            Na               {round(infile[i, 4], 10)} 
            K                {round(infile[i, 3], 10)} 

        EXCHANGE {i + 1}
            -equilibrate  {i + 1}
            X                0.0011 

        SELECTED_OUTPUT 1
            -high_precision       true
            -reset                false
            -solution             false
            -time                 false
            -pH                   true
            -pe                   true
            -totals               Ca  Cl  K  Na  
            -active               true
        END
        """
        input_string_all += input_block

    # Run PHREEQC calculation
    phreeqc_result = selected_array(db_path, input_string_all)
    species_list = list(phreeqc_result.keys())

    # Map PHREEQC results back to array
    for jj in range(outn):
        species = species_list[jj]
        values = phreeqc_result[species]
        for zz in range(m):
            phresult[zz, jj] = float(values[zz * 4 + 3])

    # Save output files
    np.savetxt(os.path.join(results_dir, '11111111.txt'), phresult)

    for i in range(m):
        for k in range(n):
            infile[i, 1 + k] = phresult[i, 2 + k] * 1000

    np.savetxt(os.path.join(results_dir, 'infile.txt'), infile)

    # Save timestamped initial conditions
    timestep = int(0.01 * 72000)
    timestamped_filename = os.path.join(results_dir, f"initcon{timestep}.txt")
    np.savetxt(timestamped_filename, infile)

    print(f"PHREEQC step 1 completed. Results saved in: {results_dir}")
    return


if __name__ == "__main__":
    phreeqc_first_step()