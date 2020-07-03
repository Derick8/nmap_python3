import nmap
import sys

if len(sys.argv)<2:
   print("usage: python3 nmaptool <url> \n" )
   sys.exit(0)
target=str(sys.argv[1])
ports=[21,22,80,139,443,8080]
scan_result=nmap.PortScanner()

for port in ports:
    portscan=scan_result.scan(target,str(port))   
    print("Port",port,portscan['scan'][list(portscan['scan'])[0]]['tcp'][port]['state'])
print("\n Host IP:",target,"is",portscan['scan'][target]['tcp'][port]['state'])
