It Seems that a fast way to learn penetration testing is to use this Framework.

## Practice

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
