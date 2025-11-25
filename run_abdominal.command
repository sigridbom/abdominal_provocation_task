#!/bin/bash
# run_experiment.sh
# Navigate to scripts folder, activate venv, and run main.py

# Exit immediately if any command fails
set -e

# Navigate to the folder containing scripts
cd "$(dirname "$0")"

# Activate the virtual environment
# Adjust the path if your venv is located elsewhere
source ./.venv/bin/activate

# Run the main experiment
python ./scripts/main.py

# Deactivate venv when done
deactivate
