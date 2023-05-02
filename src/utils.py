from os import system
from os.path import exists


def placeholder_for_testcases():
    print("------------------")


def compile_file(compiler, full_path_to_file, destination_directory, short_name):
    system('/bin/rm -f ' + destination_directory + short_name)
    system(compiler + ' ' + full_path_to_file + ' -o ' + destination_directory + short_name)
    if not exists(destination_directory + short_name):
        print("Compilation failed.")
        return 1
    return 0


def run(file_name, directory, inputs_list, interpreter=""):
    if interpreter:
        command = interpreter + " " + file_name
    else:
        command = directory + " " + file_name

    if inputs_list:
        if len(inputs_list) > 1:
            placeholder_for_testcases()
        for index, infile in enumerate(inputs_list):
            if len(inputs_list) > 1:
                print(f"# Output {index + 1}")
            system(command + ' < ' + directory + infile)
            if len(inputs_list) > 1:
                placeholder_for_testcases()
    else:
        system(command)
