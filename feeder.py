#!/usr/bin/env python

from pydbus import SessionBus
import re
import sys


bus = SessionBus()
proxy = bus.get('gent.hackerspace.pamela2')


re_mac = re.compile("([a-fA-F0-9]{0,2}:){5}[a-fA-F0-9]{0,2}")
re_ip =  re.compile("([0-9]{1,3}\.){3}[0-9]{1,3}")

def getFirstMac(aString):
    # TODO normalize mac string
    result = re_mac.search(aString)
    if result:
        mac = result.group().lower()
    else:
        mac = None
    return mac

def getFirstIP(aString):
    result = re_ip.search(aString)
    if result:
        ip = result.group()
    else:
        ip = None
    return ip

if __name__ == "__main__":
    for line in sys.stdin:
        mac = getFirstMac(line)
        if mac:
            print mac
            proxy.Macs = [mac]
        
        ip = getFirstIP(line)
        if ip:
            print ip
            proxy.IPs = [ip]
