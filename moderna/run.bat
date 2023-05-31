@echo off

:: echo that the script is going to start running.

echo "Starting Pinger Script"

:: Run the script

setlocal
%@Try%
  python trcrt.py
%@EndTry%
:@Catch
  python3 trcrt.py
:@EndCatch

