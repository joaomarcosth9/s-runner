from os import system
from os.path import exists


def placeholder_for_testcases():
    print("------------------")


def compile_file(command_to_compile, full_path_to_file, destination_directory, short_name):
    system('rm -f ' + destination_directory + short_name)
    system(command_to_compile + full_path_to_file + ' -o ' + destination_directory + short_name)
    if not exists(destination_directory+short_name):
        return 1
    return 0


def run(file_name, directory, inputs_list, interpreter=""):
    if inputs_list:
        if len(inputs_list) == 1:
            if interpreter:
                system(interpreter + file_name + ' < ' + directory + inputs_list[0])
            else:
                system(directory + file_name + ' < ' + directory + inputs_list[0])
        else:
            placeholder_for_testcases()
            for index, infile in enumerate(inputs_list):
                print(f"# Output {index + 1}")
                if interpreter:
                    system(interpreter + file_name + ' < ' + directory + infile)
                else:
                    system(directory + file_name + ' < ' + directory + infile)
                placeholder_for_testcases()
    else:
        system(interpreter + file_name)
