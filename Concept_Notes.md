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
        * Frames are used to communicate <b>within broadcast domains<b> or locations <b>inside default gateways></b, or <b>prior to passing a router</b>
        * Once a router is passed, the router's hardware address is used for another broadcast domain
        * Man-in-the-Middle (MitM) attacks (layer 2 attack), you have to be within the broadcast domain
      * Layer 2 in wireless networks
