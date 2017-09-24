#!/usr/bin/env python

# based on the pydbus tutorial code at
# https://github.com/LEW21/pydbus/blob/master/doc/tutorial.rst

from pydbus import SessionBus
from gi.repository import GLib

def showMacs(a,b,c):
    print str(b["Macs"])

if __name__ == "__main__":
    bus = SessionBus()
    proxy = bus.get('gent.hackerspace.pamela2')

    proxy.onPropertiesChanged = showMacs

    loop = GLib.MainLoop()
    loop.run()
