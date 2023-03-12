#!/usr/bin/python3

import nmap3
nmap = nmap3.Nmap()

#Host IP address needs to be entered.
os_results = nmap.nmap_os_detection("")