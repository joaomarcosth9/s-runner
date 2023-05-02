from os.path import exists
import re
from bs4 import BeautifulSoup


from url import parse, check_page_cache


s_runner_working_directory = "/tmp/s-runner/"
test_line_delimiter = '\n'


def check_input_output_cache(problem_id):
    # Check if the problem's input and output are cached
    # and if they aren't, it does.
    full_problem_id = s_runner_working_directory + problem_id
    inputfile = full_problem_id + '.input'
    outputfile = full_problem_id + '.output'  # Currently I'm not using the output for nothing.
    if not exists(inputfile) or not exists(outputfile):
        check_page_cache(problem_id, 'codeforces')
        page_path = full_problem_id + '.html'
        try:
            with open(page_path, 'r') as problem_page_html:
                parsed_html = BeautifulSoup(problem_page_html, features='html.parser')

                # When the problem input gives a first line with the number of testcases
                # the HTML of the input section is different, this three lines verify it.
                has_first_line_testcases = parsed_html.body.find(
                    'div', attrs={'class': 'input'}).find_all(
                    'div', attrs={'class': re.compile('test-example')})

                if has_first_line_testcases:
                    all_input_boxes = parsed_html.body.findAll(
                        'div', attrs={'class': 'input'})
                    total = len(all_input_boxes)
                    with open(inputfile, 'w') as number_of_inputs:
                        for index, inputbox in enumerate(all_input_boxes):
                            with open(full_problem_id + '.in' + str(index), 'w') as inputbox_number_i:
                                parsed_testcases = inputbox.find_all(
                                    'div', attrs={'class': re.compile('test-example')})
                                for line in parsed_testcases:
                                    inputbox_number_i.write(line.text + test_line_delimiter)
                        number_of_inputs.write(str(total))
                else:
                    all_input_boxes = parsed_html.body.findAll(
                        'div', attrs={'class': 'input'})
                    total = len(all_input_boxes)
                    with open(inputfile, 'w') as number_of_inputs:
                        for index, inputbox in enumerate(all_input_boxes):
                            with open(full_problem_id + '.in' + str(index), 'w') as inputbox_number_i:
                                parsed_input = inputbox.find('pre')
                                for line in parsed_input.find_all('br'):
                                    line.replaceWith(test_line_delimiter)
                                inputbox_number_i.write(parsed_input.text)
                        number_of_inputs.write(str(total))
                outputs = parsed_html.body.findAll(
                    'div', attrs={'class': 'output'})
                with open(outputfile, 'w') as real_output_file:
                    for outputbox in outputs:
                        parsed_outputs = outputbox.find('pre')
                        for line in parsed_outputs.find_all('br'):
                            line.replaceWith(test_line_delimiter)
                        real_output_file.write(parsed_outputs.text)

        except Exception as err:
            print("Something went wrong while parsing input/output.")
            print(err)
            exit(1)

if __name__ == '__main__':
    # just for testing
    url = input()
    parsed = parse(url)
    check_input_output_cache(parsed)
