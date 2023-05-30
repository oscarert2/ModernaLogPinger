import subprocess
import datetime
import pandas as PD
import time

def datetimestring():
    newFile = str(datetime.datetime.now());
    newFile = newFile.split(".")[0]
    newFile = newFile.replace(" ", "_")
    newFile = newFile.replace(":", "_")
    newFile = newFile.replace("-", "_")
    return newFile


while True:
    ips = PD.read_csv("ips.csv")
    datestr = str(datetimestring()+".txt")
    print(datestr)

    for _, row in ips.iterrows():

        with open(datestr, "a") as out:
            ipnow = row[0]
            iploc = row[1]
            print("Tracing route to: " + ipnow + ", located in:"+ iploc + " ... this could take a while")
            console_output = subprocess.check_output("pathping -q 2 "+ ipnow, text = True, shell=True)
            lines = console_output.split("\n")
            imprime = False
            out.write("From: " + ipnow + " in: "+ iploc + "\n")
            for i, line in enumerate(lines):           
                if "Procesamiento" in line:
                    imprime = True
                if imprime:     
                            
                    print(line)              
                    out.write(line+"\n")
            out.close()
    
    time.sleep(15)
        


