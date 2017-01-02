#!/bin/bash

HOME="/home/mkluge"
LOGILE="timew.log"
TIMEW_BINARY="/usr/local/bin/timew"
PATH='/home/mkluge/bin:/usr/local/bin:/usr/bin:/cygdrive/c/Python27:/cygdrive/c/Python27/Scripts'

cd $HOME
bash -l -c "$TIMEW_BINARY $*" 1>>$LOGFILE 2>&1

