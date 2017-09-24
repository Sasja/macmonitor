#!/usr/bin/env bash

pids=$(pgrep -g $(cat ./run/pamela2.pid))

if [ -z "$pids" ]
then
    echo "starting up pamela2 service..."
else
    echo "found running processes related to service!"
    echo "pids:" $pids
    echo "please kill these first using ./stopall.sh"
    exit 1
fi

echo "starting macmonitor..."
python -u macmonitor.py > ./logs/macmonitor.log 2>&1 &
sleep 1

echo "staring auto_arpscan..."
./auto_arpscan.sh > ./logs/auto_arpscan.log 2>&1 &
echo "staring auto_arping..."
./auto_arping.sh  > ./logs/auto_arping.log  2>&1 &
echo "staring auto_dhcp..."
./auto_dhcp.sh    > ./logs/auto_dhcp.log    2>&1 &

echo "saving proces group id to './run/pamela2.pid'"
echo $$ > "./run/pamela2.pid"
