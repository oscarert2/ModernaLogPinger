import subprocess
import datetime
import pandas as pd
import sys
import os
import time

def datetimestring():
    now = datetime.datetime.now()
    return now.strftime("%Y_%m_%d_%H_%M_%S")

def trace_route(ip_address, location, output_file):
    print(f"Tracing route to: {ip_address}, located in: {location}... this could take a while")
    try:
        console_output = subprocess.check_output(f"pathping -q 4 {ip_address}", text=True, shell=True)
        lines = console_output.split("\n")
        imprime = False
        output_file.write(f"From: {ip_address} in: {location}\n")
        for line in lines:
            if imprime:
                i += 1
            if "Procesamiento" in line or "Computing" in line:
                imprime = True
                i = 0
            if imprime and i >= 3:
                print(line)
                output_file.write(line + "\n")
    except subprocess.CalledProcessError as e:
        print(f"Error tracing route to {ip_address}: {e}")
        output_file.write(f"Error tracing route to {ip_address}: {e}\n")

def main():
    INPUT_FILE_NAME = "ips.csv"

    if not os.path.isfile(INPUT_FILE_NAME):
        print(f"Error: {INPUT_FILE_NAME} does not exist")
        sys.exit(1)

    ips = pd.read_csv(INPUT_FILE_NAME)

    while True:
        OUTPUT_FILE_NAME = f"./logs/{datetimestring()}.txt"

        print(f"Output file: {OUTPUT_FILE_NAME}")

        for _, row in ips.iterrows():

            with open(OUTPUT_FILE_NAME, "a") as output_file:
                trace_route(row[0], row[1], output_file)
                output_file.close()
        
        time.sleep(2)

if __name__ == "__main__":

    main()
       