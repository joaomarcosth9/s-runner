import os

def placeholder_for_testcases():
    print("------------------")

def compile(command_to_compile, full_path_to_file, working_directory, short_name):
    os.system(command_to_compile + full_path_to_file + ' -o ' + working_directory + short_name)

def run_compiled(file_name, working_directory, inputs_list):
    if inputs_list:
        if len(inputs_list) == 1:
            os.system(working_directory + file_name + ' < ' + working_directory + inputs_list[0])
        else:
            placeholder_for_testcases()
            for infile in inputs_list:
                print(f"# Input {inputs_list.index(infile) + 1}")
                os.system(working_directory + file_name + ' < ' + working_directory + infile)
                placeholder_for_testcases()
    else:
        os.system(working_directory + file_name)

def run_interpreted(interpreter, full_path_to_file, working_directory, inputs_list):
    if inputs_list:
        if len(inputs_list) == 1:
            os.system(interpreter + full_path_to_file + ' < ' + working_directory + inputs_list[0])
        else:
            placeholder_for_testcases()
            for infile in inputs_list:
                print(f"# Input {inputs_list.index(infile) + 1}")
                os.system(interpreter + full_path_to_file + ' < ' + working_directory + infile)
                placeholder_for_testcases()
    else:
        os.system(interpreter + full_path_to_file)
