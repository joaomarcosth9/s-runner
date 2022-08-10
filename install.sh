#!/bin/bash

ok="[OK]"
ast="[*]"
error="[X]"

if [[ ! $(command -v python) =~ 'python' ]]
then
    echo -e "\n$error Python not found...\n"
    sleep 1
    exit
fi

if [[ ! $(command -v git) =~ 'git' ]]
then
    echo -e "\n$error Git not found...\n"
    sleep 1
    exit
fi

echo -e "\n$ast Starting install!\n"
sleep 1

cd /opt
if [[ -d "/opt/s-runner" ]]
then
    sudo rm -rf /opt/s-runner
fi
sudo git clone https://github.com/joaomarcosth9/s-runner/
sudo chmod +x /opt/s-runner/src/s.py
if [[ -f "/usr/bin/s" ]]
then
    sudo rm -rf /usr/bin/s
fi
sudo ln -s /opt/s-runner/src/s.py /usr/bin/s

echo -e "\n$ok Installed at /opt/s-runner!\n"
