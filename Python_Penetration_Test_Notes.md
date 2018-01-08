

***************************************************************************

OVERVIEW

* Python, Ruby and Perl are <b>interpreted languages</b>, the code will be turned into machine leanguage and execute. C, C++ are compiled languages, they will be compiled before running, and therefore they are faster. But, compiled code is generated for a specific system type and distribution, cannot be moved through a geterogeneous environment (an environment that has ultiple system types and different distributions), while interpreted code can be portable as long as the interpreter is avilable.
* Python is Dynamiclly Typed, which means variables are interpreted at runtime, so you don't need to define variable size or type

***************************************************************************

BASICS BUT MORE SECURE

* Better to put `#!/usr/bin/env python` at the top of each python file, so that OS (Linux, Unix, OSX) can determine which interpreter to run absed on what is set in `PATH` environment variable. Windows will ignore this line and treat it as a comment.

***************************************************************************

PYTHON NMAP

* Download & Install nmap: https://nmap.org/book/inst-macosx.html 
* Type in your terminal `nmap --version`, if it will show a version then you installed successfully
* Type `pip install python-nmap`, https://pypi.python.org/pypi/python-nmap
* My python nmap code: https://github.com/hanhanwu/Hanhan_Penetration_Testing_Practice/blob/master/python_nmap.py
  * Credential attack reference: https://raw.githubusercontent.com/funkandwagnalls/pythonpentest/master/ssh_login.py
    * You collect (host,ssh_hosts,port_num) that with port opened
    * About netifaces: https://pypi.python.org/pypi/netifaces
    * Always change your default password; otherwise, you may be a victim. 
    * Also change your Kali instance hostname to something defensive network tools will not pick up, and always test your exploits prior to usage.

***************************************************************************

PYTHON SCAPY

* NOTE: <b>Scapy</b> is a Python program that enables the user to send, sniff and dissect and forge network packets. This capability allows construction of tools that can probe, scan or attack networks. <b>Scrapy</b> is the tool used for web parsing.
* Python Scapy: http://scapy.readthedocs.io/en/latest/introduction.html#about-scapy
* Scapy GitHub: https://github.com/secdev/scapy
* In TCP packets, different flags are in different position, you need to calculate the value for those positions
![TCP Packets](https://github.com/hanhanwu/Hanhan_Penetration_Testing_Practice/blob/master/TCP_flags.png)
  * In this TCP packets table, if you are looking for ACK, you will see value 16; if you are lokking for ACK + SYN, you will get 16+2=18
* `sr()` is for layer 3; `srp()` is for layer 2
* If a method has `1` before `()`, such as `sr1()`, it means return only the first answer
* `send()` method is used for layer 2, 3 and above
* `sendp()` uses a custom layer 2 header. `Ether()` represents the Ethernet frame header, and useful for wirelessnetworks or locations where Virtual Local Area Networks (VLANs) are used to segment networks. Wireless and VLANs are in layer 2.
* My code: https://github.com/hanhanwu/Hanhan_Penetration_Testing_Practice/blob/master/python_scapy.py
  * To be honest, not very lucky to get response from the target host, most of the time I got error. Even after I got the response, I dind't get any port scanned result
  
***************************************************************************

CREDENTIAL ATTACKS

* US Census - Surnames: https://www2.census.gov/topics/genealogy/
  * You download the surnames here, and add 26 alphabet character a-z before each surname one by one, many username for company emails will be formed in this way.
  * But it only works for English names. Meanwhile, many companies do not use this method, it can be "firstname_last_name", "firstname.lastname", etc. So, if you really want to generate the usernames for a specific company, google that company first, find some example email usernames
  * My code: https://github.com/hanhanwu/Hanhan_Penetration_Testing_Practice/blob/master/generate_basic_usernames.ipynb
