#!/usr/bin/env bash

interface=wlp3s0

while true
do
    echo "========== Running arp-scan -" "$(date)" "=========="
    arp-scan --interface="$interface" --localnet --interval=250 --random --ignoredups | ./feeder.py
    sleep 5
done
