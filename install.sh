#!/bin/bash

ok="[OK]"
ast="[*]"
error="[X]"

if [[ ! $(command -v git) =~ 'git' ]]
then
    echo -e "\n$error Git not found...\n"
    sleep 1
    exit
fi

if [[ ! $(command -v python) =~ 'python' && ! $(command -v python3) =~ 'python3' ]]
then
    echo -e "\n$error Python not found...\n"
    sleep 1
    exit
fi

echo -e "\n$ast Starting install!\n"
sleep 1

if [[ ! -d "/opt" ]]
then
    sudo mkdir /opt
fi

if [[ -d "/opt/s-runner" ]]
then
    sudo /bin/rm -rf /opt/s-runner
fi

cd /opt

sudo git clone https://github.com/joaomarcosth9/s-runner/
sudo chmod +x s-runner/src/s.py

if [[ -f "/usr/bin/s" ]]
then
    sudo /bin/rm -f /usr/bin/s
fi

if [[ ! -d "/usr/local/bin" ]]
then
    sudo mkdir /usr/local/bin
fi

if [[ -f "/usr/local/bin/s" ]]
then
    sudo /bin/rm -f /usr/local/bin/s
fi

sudo ln -s /opt/s-runner/src/s.py /usr/local/bin/s

if [[ -f "$HOME/.s-runner.json" ]]
then
    /bin/rm -f $HOME/.s-runner.json
fi

cp /opt/s-runner/languages.json $HOME/.s-runner.json

echo -e "\n$ok Installed at /opt/s-runner!\n"
