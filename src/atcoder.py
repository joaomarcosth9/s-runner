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
    # To speed up and not having to access atcoder.jp every time,
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
            print("Something went wrong while checking atcoder page.")
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
                all_sections = parsed_html.body.findAll(
                    'section')
                all_input_boxes = []
                all_output_boxes = []
                for section in all_sections:
                    if 'Sample Input' in section.text:
                        all_input_boxes.append(section.find('pre').text)
                    elif 'Sample Output' in section.text:
                        all_output_boxes.append(section.find('pre').text)
                # print(inputs)
                # print(outputs)

                total = len(all_input_boxes)
                with open(inputfile, 'w') as number_of_inputs:
                    for inputbox in all_input_boxes:
                        with open(full_problem_id+'.in'+str(all_input_boxes.index(inputbox)), 'w') as inputbox_number_i:
                                inputbox_number_i.write(inputbox)
                    number_of_inputs.write(str(total))
                with open(outputfile, 'w') as real_output_file:
                    for outputbox in all_output_boxes:
                        real_output_file.write(outputbox)

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
