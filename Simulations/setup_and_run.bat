@echo off

REM Step 1: Create a virtual environment
python -m venv venv

REM Step 2: Activate the virtual environment
call venv\Scripts\activate

REM Step 3: Install dependencies
pip install --upgrade pip
pip install MIS_algorithms
pip install pandas
pip install scipy

REM Step 4: Run your code
python compiling.py
python data_analysis_probability.py
python data_analysis_size.py

REM Step 5: Deactivate the virtual environment
deactivate