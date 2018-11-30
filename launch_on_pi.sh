#!/usr/bin/env bash

AUTO_TERRARIUM_TAG="auto_terrarium"
WEB_MONITOR_TAG="web_monitor"
DB_TAG="readings_db"
PI_SSH="ssh -t pi@raspberrypi \"cd autoterrarium\""
AT_NETWORK="at_net"
DB_PATH="/home/pi/.local/share/postgresql"

while getopts 'ub' opt
do
    case $opt in
        u) UPLOAD=1
            ;;
        b) BUILD=1
            ;;
        ?) printf "Usage: %s: [-u]" $(basename $0) >&2
            exit 2
            ;;
    esac
done
shift $(($OPTIND -1))

if [ "$UPLOAD" ]
then
    # I know this is dumb and inefficient
    ssh pi@raspberrypi "rm -rf /home/pi/auto_terrarium"
    scp -pr . pi@raspberrypi:/home/pi/auto_terrarium
fi

if [ "$BUILD" ]
then
    # Just be dumb for now and build all??
    # Build the auto_terrarium app
    ssh -t pi@raspberrypi "cd /home/pi/auto_terrarium/auto_terrarium; docker build -t $AUTO_TERRARIUM_TAG ."

    # Use port of PostgreSQL image for RPi
    ssh -t pi@raspberrypi "docker pull tobi312/rpi-postgresql"
    ssh -t pi@raspberrypi "mkdir -p $DB_PATH"
    ssh -t pi@raspberrypi "docker network create $AT_NETWORK"

    ssh -t pi@raspberrypi "cd /home/pi/auto_terrarium/web_monitor; docker build -t $WEB_MONITOR_TAG ."

fi

ssh -t pi@raspberrypi "cd /home/pi/auto_terrarium/auto_terrarium; docker run -d -p 3690:3690 --network=$AT_NETWORK $AUTO_TERRARIUM_TAG"
# ssh -t pi@raspberrypi "cd /home/pi/auto_terrarium/