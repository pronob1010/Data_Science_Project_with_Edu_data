import nmap
ns =  nmap.PortScanner().nmap_version()
ns.scan('192.185.115.123')
print(ns.scaninfo())
print(ns)
print(ns.csv())

