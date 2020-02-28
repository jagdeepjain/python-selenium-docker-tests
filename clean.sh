#!/bin/sh
if [[ $(docker ps -aq) ]]; then
    echo "Removing $(docker ps --format "{{.Names}}")..."
    running_container="$(docker ps --format "{{.Names}}")"
    docker rm -f $running_container | echo "removed..."
else
    echo "nothing to stop/remove..."
fi
