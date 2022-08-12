import requests
from os.path import exists
import re

try:
    from BeautifulSoup import BeautifulSoup # not sure if this is needed
except ImportError:
    from bs4 import BeautifulSoup

bar = "___s-runner___" # what will replace the '/' character in URL parsing
s_runner_working_directory =  "/tmp/s-runner/"
test_line_delimiter = '\n'

def parse(url):
    url = url.split('//')[-1] # remove http(s) protocol
    url = url.replace('/',bar)
    return url

def unparse(url):
    url = url.replace(bar,'/')
    url = "http://"+url # add http protocol
    return url

def check_page_cache(problem_id):
    # To speed up and not having to access codeforces.com every time,
    # the problem page is cached. This function verifies if it's already
    # cached, and if it isn't, it does.
    full_problem_id = s_runner_working_directory+problem_id
    path = full_problem_id+'.html'
    if not exists(path):
        try:
            problem_page = requests.get(unparse(problem_id))
            if problem_page.status_code != 200:
                raise Exception("Can't reach site URL.")
            html = problem_page.text
            with open(path, 'w') as file:
                file.write(html)
        except Exception as error:
            print("Something went wrong while checking codeforces page.")
            print(error)
            exit(1)

def check_input_output_cache(problem_id):
    # Check if the problem's input and output are cached
    # and if they aren't, it does.
    full_problem_id = s_runner_working_directory+problem_id
    inputfile = full_problem_id+'.input'
    outputfile = full_problem_id+'.output' # Currently i'm not using the output for nothing actually.
    if not exists(inputfile) or not exists(outputfile):
        check_page_cache(problem_id)
        page_path = full_problem_id+'.html'
        try:
            with open(page_path, 'r') as problem_page_html:
                parsed_html = BeautifulSoup(problem_page_html, features='html.parser')

                # When the problem input gives a first line with the number of testcases
                # the HTML of the input section is different, this three lines verify it.
                has_first_line_testcases = parsed_html.body.find(
                    'div',attrs={'class':'input'}).find_all(
                        'div',attrs={'class':re.compile('test-example')})

                if has_first_line_testcases:
                    all_input_boxes = parsed_html.body.findAll(
                        'div',attrs={'class':'input'})
                    total = len(all_input_boxes)
                    with open(inputfile, 'w') as number_of_inputs:
                        for index, inputbox in enumerate(all_input_boxes):
                            with open(full_problem_id+'.in'+str(index), 'w') as inputbox_number_i:
                                parsed_testcases = inputbox.find_all(
                                    'div',attrs={'class':re.compile('test-example')})
                                for line in parsed_testcases:
                                    inputbox_number_i.write(line.text+test_line_delimiter)
                        number_of_inputs.write(str(total))
                    outputs = parsed_html.body.findAll(
                        'div',attrs={'class':'output'})
                    with open(outputfile, 'w') as real_output_file:
                        for outputbox in outputs:
                            parsed_outputs = outputbox.find('pre')
                            for line in parsed_outputs.find_all('br'):
                                line.replaceWith(test_line_delimiter)
                            real_output_file.write(parsed_outputs.text)

                else:
                    all_input_boxes = parsed_html.body.findAll(
                        'div',attrs={'class':'input'})
                    total = len(all_input_boxes)
                    with open(inputfile, 'w') as number_of_inputs:
                        for index, inputbox in enumerate(all_input_boxes):
                            with open(full_problem_id+'.in'+str(index), 'w') as inputbox_number_i:
                                parsed_input = inputbox.find('pre')
                                for line in parsed_input.find_all('br'):
                                    line.replaceWith(test_line_delimiter)
                                inputbox_number_i.write(parsed_input.text)
                        number_of_inputs.write(str(total))
                    outputs = parsed_html.body.findAll(
                        'div',attrs={'class':'output'})
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


# Future feature
# def is_codeforces_file(file):
#     with open(file, 'r') as source_code:
#         if 'codeforces' in file.readlines()[0]:
#             return True
#         else:
#             return False


if __name__ == '__main__':
    # just for testing
    url = input()
    parsed = parse(url)
    check_input_output_cache(parsed)
