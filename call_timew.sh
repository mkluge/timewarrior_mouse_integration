#!/bin/bash

export LOGFILE=timew.log
export TIMEW_BINARY=/usr/local/bin/timew
export PATH=$PATH:/home/mkluge/bin:/usr/local/bin:/usr/bin:/cygdrive/c/Python27:/cygdrive/c/Python27/Scripts

cd $HOME
touch $LOGFILE
echo `date` >>$LOGFILE 2>&1
bash -l -c "$TIMEW_BINARY $*" 1>>$LOGFILE 2>&1

