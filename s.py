#!/usr/bin/python3

import argparse
from os.path import exists
from os import mkdir

import utils
import codeforces

parser = argparse.ArgumentParser(description='s-runner by joaomarcosth9',
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('path', help='path to the source code file')
parser.add_argument('-r', '--run', action='store_true', help='run the executable after compiling')
parser.add_argument('-f', '--fast', action='store_true', help='compile with less debugging flags (cpp only)')
parser.add_argument('-i', '--inputs',nargs='+', default=None, help='input files (should be located at /tmp/)')
parser.add_argument('-cf', '--codeforces', default=None, help='codeforces problem URL for automatic testing')
args = vars(parser.parse_args())

full_filename = args['path']
run = args['run']
cppfast = args['fast']
inputs = args['inputs']
cf = args['codeforces']
wd = '/tmp/'

name, file_extension = full_filename.split('/')[-1].split('.')

if cf:
    run = True
    wd = '/tmp/s-runner/'
    if not exists(wd):
        mkdir(wd)
    problem = codeforces.parse(cf)
    codeforces.check_input_output(problem)
    new_inputs = []
    with open(wd+problem+'.input', 'r') as nuinput:
        number = int(nuinput.read())
        for i in range (1,number+1):
            new_inputs.append(problem+'.in'+str(i))
            inputs = new_inputs

if file_extension == 'cpp':
    if cppfast:
        command = 'g++ -std=c++17 -O2 -w '
    else:
        # The "DLOCAL_DEBUG" flag is used for my debugging template, if you have
        # one, change it. If you don't, you can just leave as it is.
        command = 'g++ -std=c++17 -Wshadow -O2 -Wall -Wextra -Wno-unused-result -fsanitize=address -fsanitize=undefined -fno-sanitize-recover -DLOCAL_DEBUG '
    utils.compile(command, full_filename, name, wd)
    if(run):
        utils.run_compiled(name, wd, inputs)

elif file_extension == 'c':
    command = 'gcc -lm '
    utils.compile(command, full_filename, wd, name)
    if(run):
        utils.run_compiled(name, wd, inputs)

elif file_extension == 'py':
    command = 'python3 '
    utils.run_interpreted(command, full_filename, wd, inputs)

elif file_extension == 'rb':
    command = 'ruby '
    utils.run_interpreted(command, full_filename, wd, inputs)

else:
    print("Filetype not supported.")
