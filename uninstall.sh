#!/bin/bash

ok="[OK]"
ast="[*]"
error="[X]"

echo -e "\n$ast Starting uninstall.\n"
sleep 1

cd /opt
if [[ -d "/opt/s-runner" ]]
then
    sudo rm -rf /opt/s-runner
fi
if [[ -f "/usr/bin/s" ]]
then
    sudo rm -rf /usr/bin/s
fi
echo -e "$ok Uninstalled.\n"
