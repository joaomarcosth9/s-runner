import os

def placeholder():
    print("------------------")

def compile(command_to_compile, full_path_to_file, short_name):
    os.system(command_to_compile + full_path_to_file + ' -o /tmp/' + short_name)

def run_compiled(short_name, inputs):
    if inputs:
        if len(inputs) == 1:
            os.system('/tmp/' + short_name + ' < /tmp/' + inputs[0])
        else:
            placeholder()
            for infile in inputs:
                print(f"# Input {inputs.index(infile) + 1}")
                os.system('/tmp/' + short_name + ' < /tmp/' + infile)
                placeholder()
    else:
        os.system('/tmp/' + short_name)

def run_interpreted(interpreter, full_path_to_file, inputs):
    if inputs:
        if len(inputs) == 1:
            os.system(interpreter + full_path_to_file + ' < /tmp/' + inputs[0])
        else:
            placeholder()
            for infile in inputs:
                print(f"# Input {inputs.index(infile) + 1}")
                os.system(interpreter + full_path_to_file + ' < /tmp/' + infile)
                placeholder()
    else:
        os.system(interpreter + full_path_to_file)
