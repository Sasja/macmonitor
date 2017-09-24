#!/usr/bin/env python

# based on the pydbus tutorial code at
# https://github.com/LEW21/pydbus/blob/master/doc/tutorial.rst

from pydbus import SessionBus

if __name__ == "__main__":
    bus = SessionBus()
    proxy = bus.get('gent.hackerspace.pamela2')

    for mac in proxy.Macs:
        print mac
