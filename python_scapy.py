#!/usr/bin/env python

# I'm trying scapy here
# Scapy GitHub: https://github.com/secdev/scapy
# To install: git clone https://github.com/secdev/scapy
# To run: 
## cd scapy
## ./run_scapy

# In stead of running directly, you can also try (but do this under folder scapy/)
from scapy.all import *
conf.verb = 0

p = IP(dst="github.com")/ICMP()
r = sr1(p)
print r.summary()

# send a packet and get response
p = IP(dst="github.com")/ICMP()  # create a packet that contains communication details and flags to send to the target host
r = sr1(p, timeout=10)  # get response, better to have timeout here, otherwise may run forever
# Sometimes this may give you an error. But if you try later, you maybe able to send a packet

# check whether the host is up
if r is None:
  print 'The host is down'
else:
  print 'The host is up'
  
answered,unanswered = sr1(r, timout=10)  # seperate answered and unanswered data, this dind't work for me to be honest...
sent, received = answered[80]  # if you are lucky, you can check the scan results for a port, port 80 here



