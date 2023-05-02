#!/usr/bin/env python3

# official modules imports
import argparse
import json
from os.path import exists
from os import mkdir, system

# local modules imports
import utils

# command line arguments
parser = argparse.ArgumentParser(description='s-runner by joaomarcosth9',
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('path', help='path to the source code file')
parser.add_argument('-c', '--compile', action='store_true', help='just compile the file')
parser.add_argument('-f', '--fast', action='store_true', help='compile with less debugging flags (cpp only)')
parser.add_argument('-i', '--inputs', nargs='+', default=None, help='path to input files')
parser.add_argument('-p', '--problem', default=None, help='problem URL for automatic testing (codeforces and atcoder)')
parser.add_argument('-std', '--stdc++', default=20, help='C++ version')
args = vars(parser.parse_args())

# Putting command line arguments into variables
path_to_file = args['path']
run_file = not args['compile']
cpp_fast_compiling = args['fast']  # less g++ parameters (faster, but less safe)
inputs_list = args['inputs']
problem_url = args['problem']
cpp_version = args['stdc++']
s_runner_working_directory = '/tmp/'  # directory to throw compiled binaries, inputs and etc
is_compiled_language = 1  # will make more sense later
command = ""
interpreter = ""

file_name, file_extension = path_to_file.split('/')[-1].split('.')

if not exists(path_to_file):
    print(f"File {path_to_file} not found")
    exit(1)

if cpp_fast_compiling:
    if file_extension != 'cpp':
        print("Fast compiling is only available for C++ files.")
        exit(1)
    TYPE = 'fast'
else:
    TYPE = 'default'

if inputs_list:
    run_file = True

HOME = system('echo $HOME')

with open('HOME/.s-runner.json', 'r') as languages:
    languages = json.load(languages)

try:
    if problem_url:
        # If the -p flag is enabled, almost all other flags will be overwritten by those below,
        # the file will run after compiling and testcases will be scrapped from the online judge
        run_file = True
        if not exists('/tmp/s-runner'):
            mkdir('/tmp/s-runner')
        s_runner_working_directory = '/tmp/s-runner/'
        if 'codeforces' in problem_url:
            from codeforces import parse, check_input_output_cache
        elif 'atcoder' in problem_url:
            from atcoder import parse, check_input_output_cache
        else:
            raise Exception("Invalid URL.")
        problem_id = parse(problem_url)
        check_input_output_cache(problem_id)
        inputs_list = []
        with open(s_runner_working_directory + problem_id + '.input', 'r') as number_of_inputs:
            number = int(number_of_inputs.read())
            for i in range(0, number):
                inputs_list.append(problem_id + '.in' + str(i))
except Exception as error:
    print(error)
    exit(1)

if system('uname -s') == 'Darwin':
    OS = 'mac'
else:
    OS = 'linux'

try:
    if languages['compiled'].count(file_extension):
        command = languages['compiled'][file_extension][TYPE][OS]
        if file_extension == 'cpp':
            command = command.append(' --std=c++' + cpp_version)
        utils.compile_file(command, path_to_file, s_runner_working_directory, file_name)
    else:
        interpreter = languages['interpreted'][file_extension][OS]

    utils.run(file_name, s_runner_working_directory, inputs_list, interpreter)

except Exception as error:
    system("/bin/rm -rf /tmp/s-runner/*")
    print(error)
    exit(1)
