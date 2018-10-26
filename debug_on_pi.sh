#!/bin/bash

HOST=pi
HOSTNAME=raspberrypi
DEBUG_SRC="dht/ccode"

scp -r $DEBUG_SRC $HOST@$HOSTNAME:/tmp/

ssh $HOST@$HOSTNAME 'cd /tmp/ccode; make debug; gdb debug'
