#!/usr/bin/env python

# based on the pydbus tutorial code at
# https://github.com/LEW21/pydbus/blob/master/doc/tutorial.rst

from pydbus import SessionBus
from pydbus.generic import signal
from gi.repository import GLib
from time import time, strftime

mactimeout = 30
iptimeout = 120

interfacename = "gent.hackerspace.pamela2"

def mylog(eventString):
    print strftime('%X %x %Z') + ": " + eventString

class MyInterface(object):
    """
      <node>
        <interface name='gent.hackerspace.pamela2'>
          <property name="Macs"  type="as"   access="readwrite">
              <annotation name="org.freedesktop.DBus.Property.EmitsChangedSignal" value="true"/>
          </property>
          <property name="IPs"   type="as"   access="readwrite"/>
        </interface>
      </node>
    """

    def __init__(self):
        self._macs = {}
        self._ips = {}

    @property
    def Macs(self):
        return self._macs.keys()

    @Macs.setter
    def Macs(self, values):
        newMac = False
        for v in values:
            if not v in self._macs.keys():
                newMac = True
                mylog("new " + v)
            self._macs[v] = time() + mactimeout
        if newMac:
            self.PropertiesChanged(interfacename, {"Macs": self.Macs}, [])

    @property
    def IPs(self):
        return self._ips.keys()

    @IPs.setter
    def IPs(self, values):
        for v in values:
            if not v in self._ips.keys():
                mylog("new " + v)
            self._ips[v] = time() + iptimeout

    def updateTimeouts(self):
        now = time()
        change = False
        for mac in self._macs.keys():
            if now > self._macs[mac]:
                del self._macs[mac]
                change = True
                mylog("deleting " + mac)
        if change:
            self.PropertiesChanged(interfacename, {"Macs": self.Macs}, [])
        for ip in self._ips.keys():
            if now > self._ips[ip]:
                del self._ips[ip]
                mylog("deleting " + ip)

    PropertiesChanged = signal()

def tickCallback( myObject ):
    myObject.updateTimeouts()
    return True

if __name__ == "__main__":
    bus = SessionBus()

    myObject = MyInterface()
    bus.publish(interfacename, myObject)
    GLib.timeout_add(1000, tickCallback, myObject)

    loop = GLib.MainLoop()
    loop.run()
