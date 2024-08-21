#!/bin/bash

# Step 1: Create a virtual environment
python3 -m venv venv

# Step 2: Activate the virtual environment
source venv/bin/activate

# Step 3: Install dependencies
pip install --upgrade pip
pip install MIS_algorithms
pip install pandas

# Step 4: Run your code
python compiling.py

# Step 5: Deactivate the virtual environment
deactivate