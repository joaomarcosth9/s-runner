from os import system

def placeholder_for_testcases():
    print("------------------")

def compile(command_to_compile, full_path_to_file, destination_directory, short_name):
    system(command_to_compile + full_path_to_file + ' -o ' + destination_directory + short_name)

def run_compiled(file_name, directory, inputs_list):
    if inputs_list:
        if len(inputs_list) == 1:
            system(directory + file_name + ' < ' + directory + inputs_list[0])
        else:
            placeholder_for_testcases()
            for infile in inputs_list:
                print(f"# Input {inputs_list.index(infile) + 1}")
                system(directory + file_name + ' < ' + directory + infile)
                placeholder_for_testcases()
    else:
        system(directory + file_name)

def run_interpreted(interpreter, full_path_to_file, input_directory, inputs_list):
    if inputs_list:
        if len(inputs_list) == 1:
            system(interpreter + full_path_to_file + ' < ' + input_directory + inputs_list[0])
        else:
            placeholder_for_testcases()
            for infile in inputs_list:
                print(f"# Input {inputs_list.index(infile) + 1}")
                system(interpreter + full_path_to_file + ' < ' + input_directory + infile)
                placeholder_for_testcases()
    else:
        system(interpreter + full_path_to_file)
