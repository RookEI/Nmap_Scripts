import nmap

scanner = nmap.PortScanner()

print("Welcome, this is a simple nmap automation tool")
print("<-------------------------------------------------->")

ip_addr = input("Please enter the IP addres you want to scan: ")
print("The IP you entered is: ", ip_addr)
type(ip_addr)

#I've removed option 3)"Comprehensive scan" as the option would utilize different TCP scans, but due to limitations only one TCP scan could be specified.

resp = input(""" \nPlease enter the type of scan you want to run
             1)SYN ACK Scan
             2)UDP Scan \n:""")

print("You have selected option: ", resp)

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS', sudo=True)
    print(scanner.scaninfo())
    print("ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
    
elif resp == '2':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sU', sudo=True)
    print(scanner.scaninfo())
    print("ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())
    
#Commented ot the Comprehensive scan portion as you can only specify one type of TCP scan

#elif resp == '3':
#    print("Nmap Version: ", scanner.nmap_version())
#    scanner.scan(ip_addr, '1-1024', '-v -sS -sW -sC -A -O', sudo=True)
#    print(scanner.scaninfo())
#    print("ip Status: ", scanner[ip_addr].state())
#    print(scanner[ip_addr].all_protocols())
#    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())


elif resp >= '4':
    print("Please enter a valid response!")