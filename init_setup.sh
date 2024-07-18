#!/bin/bash

echo [$(date +%T)]: "SCRIPT STARTS"

# Check if runtime.txt exists
if [ ! -f runtime.txt ]; then
  echo [$(date +%T)]: "ERROR: runtime.txt file not found"
  exit 1
fi

# Read the Python version from runtime.txt
_VERSION_=$(cat runtime.txt)

# Check if the version format is valid (number dot number)
if [[ ! $_VERSION_ =~ ^[0-9]+\.[0-9]+$ ]]; then
  echo [$(date +%T)]: "ERROR: Invalid Python version format in runtime.txt. Expected format: number.number (e.g., 3.7)"
  exit 1
fi

echo [$(date +%T)]: "creating environment with python ${_VERSION_}"
conda create --prefix ./env python=${_VERSION_} -y

echo [$(date +%T)]: "activate environment"
source activate ./env

echo [$(date +%T)]: "install requirements"
pip install -r requirements.txt

echo [$(date +%T)]: "SCRIPT ENDS"
