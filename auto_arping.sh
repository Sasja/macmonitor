#!/usr/bin/env bash

interface=wlp3s0

while true
do
    echo "========== Arping all known ips -" "$(date)" "=========="
    ./getips.py | while read ip
    do
        echo "                          ${ip}"
        # "-f":   stop after 1st reply
        # "-w 1": wait at most 1 sec
        arping -f -w 3 -I $interface $ip | grep "reply from" | ./feeder.py
    done
    sleep 5 
done
