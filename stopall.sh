#!/usr/bin/env bash

pidfile="./run/pamela2.pid"

echo "looking up PGID of processes in file '${pidfile}'"
pid=$(cat $pidfile) &&
echo "kill -- -${pid}" &&
kill -- -${pid}
