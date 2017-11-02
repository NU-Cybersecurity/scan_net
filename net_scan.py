#!/usr/bin/env

#IMPORT MODULES
import nmap
import os
import time
import sys

# PRINT BANNER
print"""
=======================================================

         N A T I O N A L   U N I V E R S I T Y


..######..##....##.########...#######.....##....#######.
.##....##..##..##..##.....##.##.....##..####...##.....##
.##.........####...##.....##........##....##...##.......
.##..........##....########...#######.....##...########.
.##..........##....##.....##.##...........##...##.....##
.##....##....##....##.....##.##...........##...##.....##
..######.....##....########..#########..######..#######.


                > TEAM PROJECT MEMBERS <
                   - Carl Andrew Rafael
                   - Kyle Lee
                   - Pedro Garcia

========================================================
"""

raw_input("""
The next prompt will ask you to enter an IP address or IP address range you
would like to scan.

Example of usage:
 >> 192.168.1.0-255 (for a range of addresses)
 >> 192.168.1.24    (for a single address)

Press enter to continue
""")

# Gets user input for a single IP address to scan or to scan a range of addresses
# based on the example usage above
ip_adds = raw_input("Enter the IP address or range to scan: ")

#Defines the function scan_net
#scan_net scans the IP addresses in the 192.168.1.0-255 range
def scan_net():
	nm = nmap.PortScanner()
        print("Scanning..this may take some time.")

	nm.scan(hosts=ip_adds, arguments='-n -sA -R')
	hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]

#OUTPUTS THE ONLINE HOSTS TO A .CSV FILE
	for host, status in hosts_list:
		f = open('onlinehosts.csv', 'a')
		f.write(host + ' is ' + status + '\n')

scan_net()

#END OF THE PROGRAM
print("Scan complete! The ONLINE hosts will be saved on a file called onlinehosts.csv")
raw_input("\nPress enter to exit. ")
