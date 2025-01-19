import time
import os

# List of Python scripts to run (excluding accounts.py)
scripts = ["start.py", "tasks.py", "claim.py"]

# Function to run the scripts in series
def run_scripts_in_series():
    for script in scripts:
        try:
            print(f"Running {script}...")
            os.system(f"python {script}")
            print(f"Finished {script}")
        except Exception as e:
            print(f"Error running {script}: {e}")

# Main loop to execute the scripts every 24 hours
while True:
    print("Starting script execution...")
    run_scripts_in_series()
    print("All scripts completed. Waiting for 24 hours...")
    time.sleep(24 * 60 * 60)  # Sleep for 4 hours
