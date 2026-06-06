import subprocess
import sys
import os

def run_script(script):
    print(f"\n{'='*50}")
    print(f"Running {script}...")
    print('='*50)
    result = subprocess.run([sys.executable, script], capture_output=False)
    if result.returncode != 0:
        print(f"ERROR: {script} failed with return code {result.returncode}")
        sys.exit(1)
    print(f"Completed {script}")

def run():
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    run_script("etl/eurostat_collector.py")
    run_script("etl/postal_loader.py")

    print("\n" + "="*50)
    print("Pipeline complete. Data saved to data/raw/ and data/processed/")
    print("="*50)

if __name__ == "__main__":
    run()
