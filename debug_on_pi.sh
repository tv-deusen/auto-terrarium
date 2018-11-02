#!/bin/bash

HOST=pi
HOSTNAME=raspberrypi


scp -r . $HOST@$HOSTNAME:/tmp/

ssh $HOST@$HOSTNAME "cd /tmp/auto-terrarium/"