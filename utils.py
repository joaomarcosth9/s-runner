import os
from os.path import exists

def placeholder():
    print("------------------")

def compile(command_to_compile, full_path_to_file, short_name, wd):
    os.system(command_to_compile + full_path_to_file + ' -o ' + wd + short_name)

def run_compiled(short_name, wd, inputs):
    if inputs:
        # for inp in inputs:
        #     if not exists(wd+inp):
        #         print(wd)
        #         print("Input not found")
        #         exit(1)
        if len(inputs) == 1:
            os.system(wd + short_name + ' < ' + wd + inputs[0])
        else:
            placeholder()
            for infile in inputs:
                print(f"# Input {inputs.index(infile) + 1}")
                os.system(wd + short_name + ' < ' + wd + infile)
                placeholder()
    else:
        os.system(wd + short_name)

def run_interpreted(interpreter, full_path_to_file, wd, inputs):
    if inputs:
        if len(inputs) == 1:
            os.system(interpreter + full_path_to_file + ' < ' + wd + inputs[0])
        else:
            placeholder()
            for infile in inputs:
                print(f"# Input {inputs.index(infile) + 1}")
                os.system(interpreter + full_path_to_file + ' < ' + wd + infile)
                placeholder()
    else:
        os.system(interpreter + full_path_to_file)
