@echo off

:: echo that the script is going to start running.

echo "Starting Pinger Script"

:: Run the script
cd /D "%~dp0"

setlocal
%@Try%
  python trcrt.py
%@EndTry%
:@Catch
  python3 trcrt.py
:@EndCatch

