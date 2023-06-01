import subprocess
import datetime
import pandas as pd
import sys
import os
import time
from parsertrcrt import to_json_parser

def datetimestring():
    now = datetime.datetime.now()
    return now.strftime("%Y_%m_%d_%H_%M_%S")

def trace_route(ip_address, location, output_file, OUTPUT_FILE_NAME):
    print(f"Tracing route to: {ip_address}, located in: {location}... this could take a while")
    try:
        console_output = subprocess.check_output(f"pathping -q 4 {ip_address}", text=True, shell=True)
        lines = console_output.split("\n")

        line_to_break = 0
        output_file.write(f"To: {ip_address} in: {location}\n")
        for index, line in enumerate(lines):
            if "Procesamiento" in line or "Computing" in line:
                line_to_break = index + 3
                string_to_parse = "\n".join(lines[line_to_break:])

                output_file.write(string_to_parse)
                to_json_parser(" ".join(lines[line_to_break].split()[1:]), location, string_to_parse, OUTPUT_FILE_NAME)

                break

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
        OUTPUT_FILE_NAME = f"{datetimestring()}"
        OUTPUT_FILE_PATH = f"./logs/{OUTPUT_FILE_NAME}.txt"

        print(f"Output file: {OUTPUT_FILE_PATH}")

        for _, row in ips.iterrows():

            with open(OUTPUT_FILE_PATH, "a") as output_file:
                trace_route(row[0], row[1], output_file, OUTPUT_FILE_NAME)
                output_file.close()
        
        time.sleep(2)

if __name__ == "__main__":

    main()
       