Sometimes your code is running, and you just don't want to check social media, what to do? Keep learning!

## Warning Zone! - When Working For Clients (Python Focus)
* Better to avoid to install any library on client systems, in case of adding more risks and other unintended consequences


## What is penetration testing
  * It assess an organization's security strategy's ability to protect critical data from the actions of a malicious actor, focusing on maintaining the confidentiality, integrity, and availability of the organization's critical data and resources.
    * That is to say, to understand the company's polity, strategy is more important than just findning vulnerabilities. The focus on Vulnerability Management Solution will (VMS) create much more False Positive, since the real problem can be caused by the policy/strategy, but VMS won't be able to find the souce of chained problems
    
    
## Penetration Testing Execution Standard
  * First of all, you have to be CREATIVE in each step (otherwise how could you find what attackers could find...)
  * The author suggests to  follow these phases, and try to move from one phase to the next smoothly
    * Pre-engagement Interactions
    * Intelligence Gathering
    * Threat Modeling
    * Vulnerability Analysis
    * Exploitation
    * Post Exploitation
    * Reporting
  * Pre-engagement Interactions
    * This is the plan making stage and the most important stage. The plan that best matches the work requested, price, the associated scope, timeline, and capabilities often wins. When there is change in the plan, should be documented and signed by authoritive group (haha...changes...)
    * Assessment often drops into these categories:
      * Web application
      * Internal network
      * External network
      * Physical
      * Social engineering telephony
      * Phishing
      * Voice Over Internet Protocol (VOIP)
      * Wireless
      * Mobile application
  * Intelligence Gathering
    * The data gathered here is great for building profiles for social engineering and physical engagements
  * Threat Modeling
    * Decide the malicious actor you can mimic, they can be: Nation states, Organized crime, Hackers, Script kiddies, Hacktivists, Insiders (intentional or unintentional)
  * Vulnerability Analysis
    * The part you put most of the time on
  * Exploitation
    * You actually gain the access to the system here
  * Post Exploitation
    * This is where you prove risk to an organization by proving the level of access achieved, the amount and type of critical data accessed, and the security controls bypassed
  * Reporting
    * Target Chief suite and or the Advisory Board
    * A storyline that tells what was done during the engagement, the actual security findings or weaknesses, and the positive controls that the organization has established
    * Each noted security finding better to have a screenshot


## Identify Targets
* Systems Communication
  * As a system generates data, the data is transmitted through TCP/IP stack, which packages data into something that can be transmitted through wire.
    * TCP - Transmission Control Protocol
    * IP - Internet Protocol
    * TCP/IP stack is the implementation of TCP/IP model
    * a Socket is what communication is execute through, by linking source and destination IP address, as well as source and destination ports
  * You may not need to scan ports in ephemeral port range, when you are trying to identify targets
    * Ports here are known as dynamic ports. They are short-lived and often associated with specific communication streams only
    * Services such as File Transfer Protocol (FTP) use this technique
    * Security by Bbscurity - But! Administrators may hide some services in these ports so that the services won't be identified. If you need to scan many hosts, you can avoid scanning these ports since they will cost you longer time. When you haven't identified many services, or the hosts in target network is not too much, you can scan these ports.
  * Frame Generation for the communication between 2 systems
  ![Network Frame](https://github.com/hanhanwu/Hanhan_Penetration_Testing_Practice/blob/master/network_frame.png)
  
    * Ethernet Frame
      * A frame is a way where data travels from host to host
      * Frames communicate via a hardware address known as a Media Access Control (MAC) address
      * It contains multiple components, at the end of a frame, there is checksum to check the integrity in data after it's been transmitted through wire
      * Layer 2 in Ethernet networks
        * Frames are used to communicate <b>within broadcast domains</b> or locations <b>inside default gateways</b>, or <b>prior to passing a router</b>
        * Once a router is passed, the router's hardware address is used for another broadcast domain
        * Man-in-the-Middle (MitM) attacks (layer 2 attack), you have to be within the broadcast domain
      * Layer 2 in wireless networks
        * When doing wireless attacks, the concept is similar to MitM attacks, you have to be within range of the Service Set Identifier (SSID) or the actual wireless network name
        * Communication is through AP (Access Points)
        * If a wireless network contains more than one AP, it is an ESS
        * Distribution System (DS) - a nonwireless network that connects APs
      * The IP packet architecture
        * IPv6 could open new holes without being considered carefully. For example, an organization forgot that IPv6 is supported by default and turned on, and they are using IPv4 for configeration. In this way, attack can come through without being noticed.
      * TCP
        * TCP header contains sequencing, flags and control mechanism
        * Attackers can manipulate the flags in order to get the response from target system
        * TCP is a connection-oriented protocol, and a session is established between 2 systems
        * 3 way handshake: 
          * SYN flag sent from the source system to the target systems
          * SYN-ACK sent from the target systems to the source systems
          * ACK flag sent from source systems to target systems
          * If communication was not finished, most systems nowadays will reset or close it
      * UDP
        * UDP header is smaller than TCP header, and it is a simple connectionless-oriented protocol
        * UDP establishes a communication stream with a listening port. That port accepts the data and runs it up the TCP/IP stack as necessary. While TCP is needed for synchronized and reliable communication, UDP is not.
        
    * Understand Nmap
      * [Limitation 1: Resident TCP/IP stack] - It's using the integrated TCP/IP stack of the host operating system.
        * DON'T scan more than once at a time for the same host. Execute only one instance of an nmap scan per host. Otherwise, it can slow down the execution but also creates errors, since each received packet can impact the results depending on the instance it was received by
        * Solution, if you want to scan more than once. Use nmap to execute a scan using the host TCP/IP stack and the Unicorn scan, which contains its own TCP/IP stack
      * [Limitation 2: Limitation of how detailed packets can be manipulated through nmap]
        * Solution - HPING for single host: it allows you to create customized packets
        * Solution - FPING for multiple hosts
      * Input IP ranges through comand line
        * `nmap -sS -vvv -p 80 192.168.195.0/24`, type ip ranges in comand line
        * `nmap -sS -vvv -p 80 -iL input_ip_file`, ip ranges are in a file
      * 4 primary scans
        * TCP full connection scan
          * It may provide the most accurate scan, but automatic shunning system may block the source of the scan at the Internet Service Provider (ISP)
          * `nmap -sT -vvv -p 80 192.168.195.0/24`
        * SYN scan
          * A type of TCP scan, but faster and quieter
          * Don't use it on extremely old or sensitive equipments. If the system cannot close the connection itself without receiving ACK response, there can be problems, sometimes it can be Denial of Service (DoS)
          * `nmap -sS -vvv -p 80 192.168.195.0/24`
        * ACK scan
          * Rarest TCP scan and it's slow
          * But it's good for mapping firwall rule sets
          * Some systems act in a strange way when you are doing ACK scan, so better to have `tcpdump` running or an inline tap on your system
          * `nmap -sA -vvv -p80 192.168.195.0/24`
        * UDP scans
          * Extremely slow
          * And it lies... such as it reports "filtered/open", basically means it does not know
          * Better not to use this scan in an organization, dones't have too much benefit and annoying
