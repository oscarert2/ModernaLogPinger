:: Pinger Script Installer

@echo off
:: BEGIN: installer_script

::!/bin/bash

:: Install required libraries

pip install -r requirements.txt

:: END: installer_script

echo "Finished installing required libraries"

pause

:: echo that the script is going to start running.

echo "Starting Pinger Script"

:: Run the script

python trcrt.py