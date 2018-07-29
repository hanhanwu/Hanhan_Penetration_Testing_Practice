# Hanhan_Penetration_Testing_Practice
Penetration Testing looks so cool! I also want to learn it!


*****************************************************************

INTRODUCTION

I am taking every effort to learn cyber security broader and deeper! Red team penetration testing looks so cool! I'm making progress little step by little step.


*****************************************************************

RESOURCES

Some resources only SFU students can use them. But real practical resources, I may not use SFU links.

* <b>Penetration Testing Execution Standard (PTES)</b>: http://www.pentest-standard.org/index.php/Main_Page
  * It provides detailed suggestions that feel like you are running a consultant company. Although I'm wondering how many companies will really provide so much details to a group, even it's an internal group...
  * Detailed categories of vulnerability analysis: http://www.pentest-standard.org/index.php/Vulnerability_Analysis
  

* [Metasploit: The Penetration Tester's Guide][14]
  * This maybe the best penetration testing book I have read so far. It's an old book, published in 2011, but it teaches you the fundamentals about how Metasploit works, so that no matter how fast this tool is updating, you can ramp up quickly
* [Python Penetration Testing Essentials][1]
  * Foot printing web server & application
  * Denial of Service
  * SQL Injection
* [Python Penetration Testing Essentials][4]
  * Network, Scanning, Sniffing
  * Others are similar to the above one
* [Python: Penetration Testing for Developers][2]
  * Analyzing network traffic
  * Application fingerprinting
  * Attack Scripting
  * Fuzzing & brute force
  * Reverse engineering
  * Hash
  * Screen grabing
  * Attack automation
* [Penetration Testing][3]
  * Assessment & Attacks are good to check
  * Exploits are done in Linux
* [Advanced Penetration Testing for Highly-Secured Environments: The Ultimate Security Guide][5]
  * As you can see, it's advanced!
* [Black Hat Python - 2014][13]
  * It focuses on hacking Windows
  
*****************************************************************

Power Tools

* Vulnerabilities Search: https://www.cvedetails.com

* HashCat - Cracking Passwords
  * [Github][6]
  * [All Details][7]
  * [How to use HashCat][8]
  * [HashGan Paper][12] - It says it's better than HashCat. At this moment, I didn't find the tool online or open source
  
* Metasploit - Penetrating Testing Framework
  * Official Site: https://metasploit.com/
    * Get Started: https://metasploit.com/get-started
  * [GitHub][9]
  * [Metasploitable3][10] - A VM that contains large amount of security vulnerabilities
  
* Thc-Hydra - Gain unauthorized access from remote to system
  * [GitHub][11]
  * It is proof of concept code, for leagal use only
  * In Metasploit, by default, account `msfadmin` has the same password as this username
    * Type `hydra -l msfadmin -p msfadmin -f -V 192.168.195.145 ssh`, to launch hydra to against ssh service


[1]:http://proquest.safaribooksonline.com.proxy.lib.sfu.ca/9781784398583?uicode=simonfraser
[2]:http://proquest.safaribooksonline.com.proxy.lib.sfu.ca/9781787128187?uicode=simonfraser
[3]:http://proquest.safaribooksonline.com.proxy.lib.sfu.ca/9781457185342?uicode=simonfraser
[4]:http://proquest.safaribooksonline.com.proxy.lib.sfu.ca/9781784398583?uicode=simonfraser
[5]:http://proquest.safaribooksonline.com.proxy.lib.sfu.ca/9781849517744?uicode=simonfraser
[6]:https://github.com/hashcat/hashcat
[7]:https://hashcat.net/hashcat/
[8]:https://www.youtube.com/watch?v=8fxLH-pokAI
[9]:https://github.com/rapid7/metasploit-framework
[10]:https://github.com/rapid7/metasploitable3
[11]:https://github.com/vanhauser-thc/thc-hydra
[12]:https://github.com/hanhanwu/readings/blob/master/HashGan.pdf
[13]:http://proquest.safaribooksonline.com.proxy.lib.sfu.ca/9781457189807
[14]:https://www.amazon.ca/Metasploit-Penetration-Testers-David-Kennedy/dp/159327288X

*****************************************************************

Professional Resources

* Reverse Engineering malware analysis resources: https://www.sans.org/course/reverse-engineering-malware-malware-analysis-tools-techniques
  * I means the free resources at it bottom
  
*****************************************************************

How To

* Using Free Windows XP Mode as a VMware Virtual Machine: https://zeltser.com/windows-xp-mode-for-vmware-virtualization/
* How to Get a Windows XP Mode Virtual Machine on Windows 8.1: https://zeltser.com/how-to-get-a-windows-xp-mode-virtual-machine-on-windows/
