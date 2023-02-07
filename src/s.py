#!/usr/bin/python3

# official modules imports
import argparse
from os.path import exists
from os import mkdir, system

# local modules imports
import utils

# command line arguments
parser = argparse.ArgumentParser(description='s-runner by joaomarcosth9',
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('path', help='path to the source code file')
parser.add_argument('-r', '--run', action='store_true', help='run the executable after compiling')
parser.add_argument('-f', '--fast', action='store_true', help='compile with less debugging flags (cpp only)')
parser.add_argument('-i', '--inputs', nargs='+', default=None, help='input files (should be located at /tmp/)')
parser.add_argument('-p', '--problem', default=None, help='problem URL for automatic testing (codeforces and atcoder)')
args = vars(parser.parse_args())

# Putting command line arguments into variables
path_to_file = args['path']
want_to_run_after_compiling = args['run']
cpp_fast_compiling = args['fast']  # less g++ parameters (faster, but less safe)
inputs_list = args['inputs']
problem_url = args['problem']
s_runner_working_directory = '/tmp/'  # directory to throw compiled binaries, inputs and etc
is_compiled_language = 1  # will make more sense later
command = ""
interpreter = ""

if not exists(path_to_file):
    print(f"File {path_to_file} not found")
    exit(1)

if inputs_list:
    want_to_run_after_compiling = True

file_name, file_extension = path_to_file.split('/')[-1].split('.')

try:
    if problem_url:
        print("Currently disabled.")
        exit(0)
        # If the -p flag is enabled, almost all other flags will be overwritten by those below,
        # the file will be runned after compiling and test cases will be scrapped from the online judge
        want_to_run_after_compiling = True
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
        with open(s_runner_working_directory+problem_id+'.input', 'r') as number_of_inputs:
            number = int(number_of_inputs.read())
            for i in range(0, number):
                inputs_list.append(problem_id+'.in'+str(i))

    # Now it's just filetype verification.
    # Currently supports C++,C, Python and Ruby, but it's really easy to add new languages.
    if file_extension == 'cpp':
        if cpp_fast_compiling:
            command = 'g++ -std=c++20 -O2 -w '
        else:
            # The "DLOCAL_DEBUG" flag is used for my debugging template, if you have
            # one, change it. If you don't, you can just leave as it is.
            command = 'g++ -std=c++20 -Wshadow -O2 -Wfatal-errors -Wall -Wextra -Wno-unused-result ' \
                      '-Wno-unused-variable -fsanitize=address -fsanitize=undefined -fno-sanitize-recover ' \
                      '-DLOCAL_DEBUG '

    elif file_extension == 'c':
        command = 'gcc -lm '

    elif file_extension == 'py':
        interpreter = 'python3 '
        is_compiled_language = 0

    elif file_extension == 'rb':
        interpreter = 'ruby '
        is_compiled_language = 0

    elif file_extension == 'hs':
        interpreter = 'ghci '
        is_compiled_language = 0

    else:
        print("Filetype not supported.")
    
    if is_compiled_language:
        if utils.compile_file(command, path_to_file, s_runner_working_directory, file_name) == 1:
            exit(1)
        path_to_file = file_name
    else:
        want_to_run_after_compiling = True

    if want_to_run_after_compiling:
        utils.run(path_to_file, s_runner_working_directory, inputs_list, interpreter)

except Exception as error:
    # In case of something going wrong, it's safer to clean the online working directory for the next executions
    system("rm -rf /tmp/s-runner/*")
    print(error)
    exit(1)
