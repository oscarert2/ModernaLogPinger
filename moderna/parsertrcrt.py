import re
import json


def to_json_parser(origin, location, input_str, file_name):

    '''
    input_str = """  0                                           LAPTOP-NG3N61A9.tol.itesm.mx [10.25.231.239] 
                                    0/   4 =  0%   |
    1    3ms     0/   4 =  0%     0/   4 =  0%  10.25.231.250 
                                    0/   4 =  0%   |
    2    3ms     0/   4 =  0%     0/   4 =  0%  10.25.173.36 
                                    0/   4 =  0%   |
    3    3ms     0/   4 =  0%     0/   4 =  0%  10.25.173.10"""
    '''

    # Split the input string into lines
    lines = input_str.split('\n')

    # Define a regular expression to extract the relevant information from each line
    regex = r'^\s*(\d+)\s+(\d+ms)?\s+(\d+/\s*\d+\s*=\s*\d+%)\s+(\d+/\s*\d+\s*=\s*\d+%)\s+(\d+\.\d+\.\d+\.\d+)\s*$'

    # Create a list to store the results
    results = {
        "Location": location,
        origin: []
    }
    # results = []

    # Loop through each line and extract the relevant information
    for line in lines:
        match = re.match(regex, line)
        if match:
            result = {
                'hop': int(match.group(1)),
                'rtt': match.group(2),
                'sent_received': match.group(3),
                'lost': match.group(4),
                'ip_address': match.group(5)
            }
            results[origin].append(result)

    # Convert the results to a JSON object
    json_str = json.dumps(results)

    # Write json_str into json file
    with open(f"json_logs/{file_name}.json", "a+") as json_file:
        json_file.write("\n")
        json_file.write(json_str)
        json_file.close()

