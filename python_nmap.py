import nmap
import netifaces

scanner = nmap.PortScanner()
scanner.scan('127.0.0.1', '79')  # scan 1 port
scanner.scan('127.0.0.1', '77-99')  # scan port range

for host in scanner.all_hosts():
    print scanner[host]  # print every port info in json format
    print scanner[host].hostname()
    print scanner[host].all_protocols()
    
print scanner.csv() # print every port info row by row


gateways = {}
network_ifaces={}

# Get network interface
def get_interfaces():
    interfaces = netifaces.interfaces()
    return interfaces
  
# Get network gateways
def get_gateways():
    gateway_dict = {}
    gws = netifaces.gateways()
    for gw in gws:
        try:
            gateway_iface = gws[gw][netifaces.AF_INET]
            gateway_ip, iface = gateway_iface[0], gateway_iface[1]
            gw_list =[gateway_ip, iface]
            gateway_dict[gw]=gw_list
        except:
            pass
    return gateway_dict
  
# Get hwaddr, iface_addr, iface_broadcast, iface_netmask
def get_addresses(interface):
    addrs = netifaces.ifaddresses(interface)
    link_addr = addrs[netifaces.AF_LINK]
    iface_addrs = addrs[netifaces.AF_INET]
    iface_dict = iface_addrs[0]
    link_dict = link_addr[0]
    hwaddr = link_dict.get('addr')
    iface_addr = iface_dict.get('addr')
    iface_broadcast = iface_dict.get('broadcast')
    iface_netmask = iface_dict.get('netmask')
    return hwaddr, iface_addr, iface_broadcast, iface_netmask

# For each gateway, get hwaddr, iface_addr, iface_broadcast, iface_netmask
def get_networks(gateways_dict):
    networks_dict = {}
    for key, value in gateways.iteritems():
        gateway_ip, iface = value[0], value[1]
        hwaddress, addr, broadcast, netmask = get_addresses(iface)
        network = {'gateway': gateway_ip, 'hwaddr' : hwaddress, 'addr' : addr, '                                                                                        broadcast' : broadcast, 'netmask' : netmask}
        networks_dict[iface] = network
    return networks_dict
  
# Collect host (those are not your host) with open port
def target_identifier(user,passwd,ips,port_range,ifaces):
    bufsize = 0
    scanner = nmap.PortScanner()
    scanner.scan(ips, port_range)
    
    all_hosts = scanner.all_hosts()
    
    if scanner.all_hosts():
        for host in all_hosts:
            for k,v in ifaces.iteritems():
                if v['addr'] == host:  # remove your own host
                    print("[-] Removing %s from target list since it belongs to your interface!") % (host)
                    host = None
            if host != None:
                if 'ssh' in scanner[host]['tcp'][int(port_num)]['name']:
                    if 'open' in scanner[host]['tcp'][int(port_num)]['state']:
                        print("[+] Adding host %s to %s since the service is active on %s") % (host,ssh_hosts,port_num)

home_dir="/root"
gateways = get_gateways()
network_ifaces = get_networks(gateways)
hosts_file = target_identifier(home_dir,[machine user name],[machine password],hosts,ports,network_ifaces)
