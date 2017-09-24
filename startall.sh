#!/usr/bin/env bash

echo "starting macmonitor"
python -u macmonitor.py > ./logs/macmonitor.log 2>&1 &
sleep 1

echo "staring auto_arpscan"
./auto_arpscan.sh > ./logs/auto_arpscan.log 2>&1 &
echo "staring auto_arping"
./auto_arping.sh  > ./logs/auto_arping.log  2>&1 &
echo "staring auto_dhcp"
./auto_dhcp.sh    > ./logs/auto_dhcp.log    2>&1 &

echo "saving proces group id to './run/pamela2.pid'"
echo $$ > "./run/pamela2.pid"
