#!/usr/bin/python3

import os
import sys
import argparse

parser = argparse.ArgumentParser(description='s-runner by joaomarcosth9',
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('path', help='path to the source code file')
parser.add_argument('-r', '--run', action='store_true', help='run the executable after compiling')
parser.add_argument('-f', '--fast', action='store_true', help='compile with less debugging flags (cpp only)')
parser.add_argument('-i', '--inputs',nargs='+', default=None, help='input files (should be located at /tmp/)')
args = vars(parser.parse_args())

filename = args['path']
run = args['run']
fast = args['fast']
inputs = args['inputs']
command = ''
name = ''
compiled = 0

def placeholder():
    print("------------------")

def compile():
    os.system(command + filename + ' -o /tmp/' + name)

def runn():
    if compiled:
        commandline = '/tmp/' + name
    else:
        commandline = command + filename
    if inputs:
        if len(inputs) == 1:
            os.system(commandline + ' < /tmp/' + inputs[0])
        else:
            placeholder()
            for infile in inputs:
                print(f"# Input {inputs.index(infile) + 1}")
                os.system(commandline + ' < /tmp/' + infile)
                placeholder()
    else:
        os.system(commandline)

if('.cpp' in filename):
    if fast:
        command = 'g++ -std=c++17 -Wshadow -O2 -Wno-unused-result '
    else:
        command = 'g++ -std=c++17 -Wshadow -O2 -Wall -Wextra -pedantic -g -Wformat=2 -Wfloat-equal -Wconversion -Wlogical-op -Wshift-overflow=2 -Wduplicated-cond -Wcast-qual -Wcast-align -D_GLIBCXX_DEBUG -D_GLIBCXX_DEBUG_PEDANTIC -D_FORTIFY_SOURCE=2 -fsanitize=address -fsanitize=undefined -fno-sanitize-recover -fstack-protector -DLOCAL_DEBUG '
    name = filename.split('/')[-1][:-4]
    compile()
    compiled = 1
    if(run):
        runn()

elif('.c' in filename):
    command = 'gcc -lm '
    name = filename.split('/')[-1][:-2]
    compile()
    compiled = 1
    if(run):
        runn()

elif('.py' in filename):
    command = 'python3 '
    runn()

elif('.rb' in filename):
    command = 'ruby '
    runn()

else:
    print("Filetype not supported.")
