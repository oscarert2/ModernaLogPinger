# Moderna Ping 2 Log

Moderna Ping 2 Log

ModernaLogPinger is a Python script that traces the route to a list of IP addresses and logs the results to a file. This script uses the pathping command to trace the route to each IP address in the list, and logs the output to a file.

Requirements

Windows. Python 3.x. Pandas

Installation

Clone the repository to a local machine in the outermost layer of the network topology.
Edit the CSV file containing a list of the IP addresses to be pinged and their locations*.
Run the script by executing the file called install.bat (if its your first time runing the script) or the run.bat file after youve installed the dependecies.
The script will trace the route to each IP address in the list and log the results to a file inside the Log folder.

Configuration
The following variables can be configured in the script:
INPUT_FILE_NAME: The name of the CSV file containing the list of IP addresses and their locations.
OUTPUT_FILE_NAME: The name of the file to log the results to. If not specified, the script will generate a file name based on the current date and time.

Debugging:
If the run.bat file does not run the script run it manually by navigating to the folder through console and inputting the command: Python3 trcrt.py
If this doesnt work verify that the folder name Log exists in the same folder as the script.

License
This project is open source.

*The PCs that will be pinged must have a static IP address.


