#!/usr/bin/env bash

while getopts 'u' opt
do
    case $opt in
        u) UPLOAD=1
            ;;
        ?) printf "Usage: %s: [-u]" $(basename $0) >&2
            exit 2
            ;;
    esac
done
shift $(($OPTIND -1))

if [ "$UPLOAD" ]
then
    scp -pr . pi@raspberrypi:/home/pi/auto_terrarium
fi

ssh -t pi@raspberrypi "cd /home/pi/auto_terrarium; docker-compose up"