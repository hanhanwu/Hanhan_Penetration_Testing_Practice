It Seems that a fast way to learn penetration testing is to use this Framework.

## Metasploit Resources
* Exploit Database: https://www.rapid7.com/db/modules/

## Practice
To use msfconsole, type `msfconsole` in the terminal.

### Passive Information Gathering
#### whois
* whois searches for an object in a WHOIS database. WHOIS is a query and response protocol that is widely used for querying databases that store the registered users of an Internet resource, such as a domain name or an IP address block, but is also used for a wider range of other information.
* In msfconcole, type `whois secmaniac.net`, then it will show you things like the name of domain servers of www.secmaniac.net
* With netcraft, you can find it's IP, whois can also be used on IP
#### Netcraft
* http://searchdns.netcraft.com/
* You can find the IP address of a website through this tool
#### nslookup
* It is a tool built in many systems, you can find IP address of a website through this tool
* Type `nslookup` in msfconsole, then type website domain name, such as "secmaniac.net"

### Active Information Gathering
#### nmap
* Port scanning tool. Nmap lets you scan hosts to identify the services running on each, any of which might offer a way in.
* `sudo apt-get install nmap` to install namp
* `-sS` runs a stealth TCP scan that determines whether a specific TCP-based port is open
* `-Pn`, which tells nmap not to use ping to determine whether a system is running; instead, it considers all hosts “alive.” Because most networks don’t allow Internet Control Message Protocol (ICMP), which is the protocol that ping uses.
* `-oX` to generate .xml file, `nmap -Pn -sS -A -oX Subnet1 192.168.1.0/24`
* `sudo nmap -Pn -sS -A IP`, fill in the IP in this command
#### Database in Metasploit
* Install psql in Ubuntu
  * `sudo apt-get install postgresql postgresql-contrib` to install
  * `update-rc.d postgresql enable` to config psql to start up upon server root
  * `service postgresql start` to start psql
* Setup Metasploit database
  * `systemctl start postgresql` to start up the psql server
  * `msfdb init` to create and initialize the msf database
* `msfconsole` to enter into metasploit console
* `db_status` to check whether database is connected
* Import nmap output to database
  * `nmap -Pn -sS -A -oX Subnet1 192.168.1.0/24`
  * `db_import Subnet1` to import into file Subnet
  * `db_hosts -c address` to query the address from the database
* TCP Idle Scan
  * It allows you to scan the target stealthily by spoofing the IP of another host on the network.
  * First of all, locate an idle host that uses incremental IP IDs, which are used to track packet order. When you find such an idle system, the IP IDs become predictable, and you can predict the next ID.
  * When spoofing the address of an idle host while scanning a target’s responses from open ports, you can see a break in the predictability of the IP ID sequence, which indicates that you have discovered an open port, without sending any packet to the system.
  * `use auxiliary/scanner/ip/ipidseq`, this uses the scanner/ip/ipidseq module to scan for a host that fits the TCP idle scan requirements
  * `show options`
  * `set RHOSTS 192.168.1.0/24`, using RHOST to set IP range
  * `set THREADS 7` to set threads, on Unix this value is no more than 128, on Windows, it's no more than 16
  * `run`
  * `nmap -PN -sI 192.168.1.109 192.168.1.155`, to explore open ports


************************************************************************

PENETRATION TESTING STANDARDS

* The 7 main standards for penetration testing: http://www.pentest-standard.org/index.php/Main_Page
  * Pre-engagement: http://www.pentest-standard.org/index.php/Pre-engagement
    * It provided suggestions for real business operations
    * Major questions you should ask for Network Penetration Test, Web Application Penetration Test, Wireless Network Penetration Test, Physical Penetration Test, Social Engineering, Questions for Business Unit Managers, Questions for Systems Administrators
    * Sensitive test you need to communicate
  * Vulnerability Analysis: http://www.pentest-standard.org/index.php/Vulnerability_Analysis
    * I like the analysis categories they gave in vulnerability analysis
    * Active Methods
      * Network/General Vulnerability Scanners
      * Web Application Scanners
      * Network Vulnerability Scanners/Specific Protocols
    * Passive Methods
      * Check Metadata
      * Traffic Monitoring
  * Exploitation contains major exploitation methods
  * Post exploitation contains much more details, and after post exploitation, there are reports

************************************************************************

INSTALLATION

* Install on LINUX/MacOS/WINDOWS: https://github.com/rapid7/metasploit-framework/wiki/Nightly-Installers
* Metasploit download: https://www.metasploit.com/

*************************************************************************

RESOURCES/TUTORIALS

* Metasploit documents: https://metasploit.help.rapid7.com/docs/discovery-scan
* NULL BYTE tutorials: https://null-byte.wonderhowto.com/search/msf/
