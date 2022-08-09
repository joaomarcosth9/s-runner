#!/usr/bin/python3

import argparse

import utils

parser = argparse.ArgumentParser(description='s-runner by joaomarcosth9',
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('path', help='path to the source code file')
parser.add_argument('-r', '--run', action='store_true', help='run the executable after compiling')
parser.add_argument('-f', '--fast', action='store_true', help='compile with less debugging flags (cpp only)')
parser.add_argument('-i', '--inputs',nargs='+', default=None, help='input files (should be located at /tmp/)')
args = vars(parser.parse_args())

full_filename = args['path']
run = args['run']
cppfast = args['fast']
inputs = args['inputs']

name, file_extension = full_filename.split('/')[-1].split('.')

if file_extension == 'cpp':
    if cppfast:
        command = 'g++ -std=c++17 -O2 -w '
    else:
        # The "DLOCAL_DEBUG" flag is used for my debugging template, if you have
        # one, change it. If you don't, you can just leave as it is.
        command = 'g++ -std=c++17 -Wshadow -O2 -Wall -Wextra -Wno-unused-result -fsanitize=address -fsanitize=undefined -fno-sanitize-recover -DLOCAL_DEBUG '
    utils.compile(command, full_filename, name)
    if(run):
        utils.run_compiled(name, inputs)

elif file_extension == 'c':
    command = 'gcc -lm '
    utils.compile(command, full_filename, name)
    if(run):
        utils.run_compiled(name, inputs)

elif file_extension == 'py':
    command = 'python3 '
    utils.run_interpreted(command, full_filename, inputs)

elif file_extension == 'rb':
    command = 'ruby '
    utils.run_interpreted(command, full_filename, inputs)

else:
    print("Filetype not supported.")
