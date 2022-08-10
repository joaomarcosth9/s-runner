#!/usr/bin/python3

# official modules imports
import argparse
from os.path import exists
from os import mkdir,system

# local modules imports
import utils
import codeforces

# command line arguments
parser = argparse.ArgumentParser(description='s-runner by joaomarcosth9',
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('path', help='path to the source code file')
parser.add_argument('-r', '--run', action='store_true', help='run the executable after compiling')
parser.add_argument('-f', '--fast', action='store_true', help='compile with less debugging flags (cpp only)')
parser.add_argument('-i', '--inputs',nargs='+', default=None, help='input files (should be located at /tmp/)')
parser.add_argument('-cf', '--codeforces', default=None, help='codeforces problem URL for automatic testing')
args = vars(parser.parse_args())

# Putting command line arguments into variables
path_to_file = args['path']
want_to_run_after_compiling = args['run']
cpp_fast_compiling = args['fast'] # less g++ parameters (faster, but less safe)
inputs_list = args['inputs']
codeforces_online = args['codeforces']
s_runner_working_directory = '/tmp/' # directory to throw compiled binaries and etc
is_compiled_language = 1 # will make more sense later

if not exists(path_to_file):
    print(f"File {path_to_file} not found")
    exit(1)

file_name, file_extension = path_to_file.split('/')[-1].split('.')

try:
    if codeforces_online:
        # If the -cf flag is enabled, almost all other flags will be overwritten by those below,
        # the file will be runned after compiling and testscases will be scrapped from codeforces
        want_to_run_after_compiling = True
        if not exists('/tmp/s-runner'):
            mkdir('/tmp/s-runner')
        s_runner_working_directory = '/tmp/s-runner/'
        problem_id = codeforces.parse(codeforces_online)
        codeforces.check_input_output(problem_id)
        inputs_list = []
        with open(s_runner_working_directory+problem_id+'.input', 'r') as number_of_inputs:
            number = int(number_of_inputs.read())
            for i in range (1,number):
                inputs_list.append(problem_id+'.in'+str(i))

    # Now it's just filetype verification.
    # Currently supports C++,C, Python and Ruby, but it's really easy to add new languages.
    if file_extension == 'cpp':
        if cpp_fast_compiling:
            command = 'g++ -std=c++17 -O2 -w '
        else:
            # The "DLOCAL_DEBUG" flag is used for my debugging template, if you have
            # one, change it. If you don't, you can just leave as it is.
            command = 'g++ -std=c++17 -Wshadow -O2 -Wall -Wextra -Wno-unused-result -fsanitize=address -fsanitize=undefined -fno-sanitize-recover -DLOCAL_DEBUG '

    elif file_extension == 'c':
        command = 'gcc -lm '

    elif file_extension == 'py':
        command = 'python3 '
        is_compiled_language = 0

    elif file_extension == 'rb':
        command = 'ruby '
        is_compiled_language = 0

    else:
        print("Filetype not supported.")
    
    if is_compiled_language: # <-- here
        utils.compile(command, path_to_file, s_runner_working_directory, file_name)
        if(want_to_run_after_compiling):
            utils.run_compiled(file_name, s_runner_working_directory, inputs_list)
    else:
        utils.run_interpreted(command, path_to_file, s_runner_working_directory, inputs_list)
except:
    # In case of something going wrong, it's safer to clean the online working directory for the next executions
    system("rm -rf /tmp/s-runner/*")
