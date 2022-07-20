#!/usr/bin/python3

import os
import sys
import argparse

parser = argparse.ArgumentParser(description='s-runner by joaomarcosth9',
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('path', help='path to the source code file')
parser.add_argument('-r', '--run', action='store_true', help='compile and run the file')
parser.add_argument('-i', '--inputfile', default=None, help='inputfile name (should be located at /tmp/)')
args = vars(parser.parse_args())

filename = args['path']
run = args['run']
inputfile = args['inputfile']

def run_compiled(file, infile):
    if infile:
        os.system('/tmp/' + file + ' < /tmp/' + infile)
    else: 
        os.system('/tmp/' + file)

def run_interpreted(file, interpreter, infile):
    if infile:
        os.system(interpreter + file + ' < /tmp/' + infile)
    else: 
        os.system(interpreter + file)

if('.cpp' in filename):
    command = 'g++ -Wall -lm --std=c++17 '
    name = filename.split('/')[-1][:-4]
    os.system(command + filename + ' -o /tmp/' + name)
    if(run):
        run_compiled(name, inputfile)

elif('.c' in filename):
    command = 'gcc -lm '
    name = filename.split('/')[-1][:-2]
    os.system(command + filename + ' -o /tmp/' + name)
    if(run):
        run_compiled(name, inputfile)

elif('.py' in filename):
    command = 'python3 '
    run_interpreted(filename, command, inputfile)

elif('.rb' in filename):
    command = 'ruby '
    run_interpreted(filename, command, inputfile)
else:
    print("Filetype not supported.")
