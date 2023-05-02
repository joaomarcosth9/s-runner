#!/bin/bash

ok="[OK]"
ast="[*]"
error="[X]"

echo -e "\n$ast Starting uninstall.\n"

sleep 1

cd /opt

if [[ -d "/opt/s-runner" ]]
then
    sudo /bin/rm -rf /opt/s-runner
fi

if [[ -f "/usr/bin/s" ]]
then
    sudo /bin/rm -rf /usr/bin/s
fi

if [[ -f "/usr/local/bin/s" ]]
then
    sudo /bin/rm -f /usr/local/bin/s
fi

echo -e "$ok Uninstalled.\n"
