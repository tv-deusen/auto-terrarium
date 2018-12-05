#!/bin/bash

# I know this is dumb and inefficient
ssh pi@raspberrypi "rm -rf /home/pi/at_app"
scp -pr . pi@raspberrypi:/home/pi/at_app
ssh pi@raspberrypi "cd /home/pi/at_app/"