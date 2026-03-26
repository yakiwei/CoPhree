import mph
import os


def comsol_first_step(mph_name):
    """
    Initializes and solves the first COMSOL model step.
    Expects the .mph file to be located in the 'models' directory.
    """
    # Define project paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    mph_path = os.path.join(base_dir, 'models', mph_name)

    if not os.path.exists(mph_path):
        raise FileNotFoundError(f"Model file not found: {mph_path}")

    print(f"Loading model: {mph_path}")

    try:
        # Start COMSOL Client and load model
        client = mph.start()
        model = client.load(mph_path)

        print("Running physical field initialization (Step 1)...")
        model.solve()

        # Ensure the export node in COMSOL is configured correctly
        model.export()

        print("Step 1 completed successfully.")
        client.remove(model)

    except Exception as e:
        print(f"Error during COMSOL execution: {e}")
        raise


if __name__ == "__main__":
    # Replace with your actual filename for testing
    comsol_first_step("case1_init.mph")