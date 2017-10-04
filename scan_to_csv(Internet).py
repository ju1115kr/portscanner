#-*- coding:cp949 -*-
import sys
import os
import nmap
import time
from os.path import expanduser

IP = "{IP}";
SUBNET = "/20";
PORT = "21, 22, 23, 25, 53, 69, 80, 110, 111, 113, 123,135, 137, 139, 143, 161, 256, 389, 443, 445, 514, 554, 631, 636, 993, 995, 1723, 3306, 3389, 5900, 8080, 9999"

try:
    nm = nmap.PortScanner();      # instantiate nmap.PortScanner object
except nmap.PortScannerError:
    print('Nmap not found', sys.exc_info()[0])
    sys.exit(1)
except:
    print("Unexpected error:", sys.exc_info()[0])
    sys.exit(1)

def Create_Scanner(IP,PORT):
    Desktop = expanduser("~\\Desktop\\")
    f = open(Desktop+addTimestamp(IP)+".csv",'w')
    nm.scan(IP+SUBNET,PORT,"-T4 -v -O");

    for host in nm.all_hosts():
        if(host != "localhost" or host != "127.0.0.1"):
            if (nm[host].all_protocols() != []):
                print(host);
                f.write("\n"+host);
                for proto in nm[host].all_protocols():
                    lport = list(nm[host][proto].keys())
                    lport.sort();
                    for port in lport:
                        if(nm[host][proto][port]['state'] == 'open'):
                            f.write("\n\t\t\t{0}/{1}".format(port, nm[host][proto][port]['name']));
                            print("\t\t\t{0}/{1}".format(port, nm[host][proto][port]['name']));
                                                     
                
    
    print("\n"+"COMMAND: "+nm.command_line()+"\n");
    print("Nmap"+str(nm.nmap_version())+ "version\n");
    print("IP: " + IP);
    print("PORT:" + PORT);
    f.write("\n"+"COMMAND: "+nm.command_line()+"\n")
    f.write("Nmap"+str(nm.nmap_version())+ "version\n")
    f.write("IP: " + IP)
    f.write("PORT:" + PORT)

def addTimestamp(filename):
    now = time.localtime()
    timestamp = "_%04d%02d%02d" % (now.tm_year, now.tm_mon, now.tm_mday)
    return filename + timestamp

def main():        
    Create_Scanner(IP,PORT);    

if __name__ == '__main__':
    main();
