import nmap

nm = nmap.PortScanner()
nm.scan('127.0.0.1', '79')  # scan 1 port
nm.scan('127.0.0.1', '77-99')  # scan port range
