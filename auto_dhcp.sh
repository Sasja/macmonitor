#!/usr/bin/env bash

interface=wlp3s0

dhcpdump -i "$interface" | \
grep --line-buffered 'OPTION:  50' | \
while read line
do
    echo "$(date)"
    printf '%s\n' "$line"
    printf '%s\n' "$line" | ./feeder.py
    echo
done
