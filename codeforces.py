import requests
from os.path import exists
import re

try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

bar = "3ecf5d9f4e82b22c5dc5c95e2de39018"
sep = "[[SEPARATOR]]"
wd =  "/tmp/s-runner/"

def parse(url):
    url = url.split('//')[-1]
    url = url.replace('/',bar)
    return url


def unparse(url):
    url = url.replace(bar,'/')
    url = "http://"+url
    return url

def check_page_cache(problem):
    path = wd+problem+'.html'
    if not exists(path):
        try:
            problem_page = requests.get(unparse(problem))
            html = problem_page.text
            with open(path, 'w') as file:
                file.write(html)
        except Exception as error:
            print("Something went wrong while checking codeforces page...")
            print(error)
            exit(1)

def check_input_output(problem):
    inputfile = wd+problem+'.input'
    outputfile = wd+problem+'.output'
    if not exists(inputfile) or not exists(outputfile):
        check_page_cache(problem)
        path = wd+problem+'.html'
        try:
            with open(path, 'r') as htmlfile:
                parsed_html = BeautifulSoup(htmlfile, features='html.parser')

                test_case_inputs = parsed_html.body.find(
                    'div',attrs={'class':'input'}).find_all(
                        'div',attrs={'class':re.compile('test-example')})

                if test_case_inputs:
                    # first line with number of testcases
                    inputs = parsed_html.body.findAll(
                        'div',attrs={'class':'input'})
                    with open(inputfile, 'w') as file:
                        i = 1
                        for inputbox in inputs:
                            with open(wd+problem+'.in'+str(i), 'w') as inputn:
                                parsed_testcases = inputbox.find_all(
                                    'div',attrs={'class':re.compile('test-example')})
                                for line in parsed_testcases:
                                    inputn.write(line.text+' ')
                            i += 1
                        file.write(str(i-1))

                    outputs = parsed_html.body.findAll(
                        'div',attrs={'class':'output'})
                    with open(outputfile, 'w') as file:
                        for outputbox in outputs:
                            parsed_outputs = outputbox.find('pre')
                            for line in parsed_outputs.find_all('br'):
                                line.replaceWith(delimiter)
                            file.write(parsed_outputs.text)
                            # file.write(sep)

                else:
                    # no first line number of testcases
                    # possibly various input boxes
                    delimiter = '\n'
                    inputs = parsed_html.body.findAll(
                        'div',attrs={'class':'input'})
                    with open(inputfile, 'w') as file:
                        i = 1
                        for inputbox in inputs:
                            with open(wd+problem+'.in'+str(i), 'w') as inputn:
                                parsed_input = inputbox.find('pre')
                                for line in parsed_input.find_all('br'):
                                    line.replaceWith(delimiter)
                                inputn.write(parsed_input.text)
                                # inputn.write(sep)
                            i += 1
                        file.write(str(i-1))

                    outputs = parsed_html.body.findAll(
                        'div',attrs={'class':'output'})
                    with open(outputfile, 'w') as file:
                        for outputbox in outputs:
                            parsed_outputs = outputbox.find('pre')
                            for line in parsed_outputs.find_all('br'):
                                line.replaceWith(delimiter)
                            file.write(parsed_outputs.text)
                            file.write(sep)

        except Exception as err:
            print("Something went wrong while parsing input/output...")
            print(err)
            exit(1)


if __name__ == '__main__':
    # just for testing
    url = input()
    # url = "https://codeforces.com/contest/977/problem/E"
    parsed = parse(url)
    # print(f"Parsed {parsed}")
    check_input_output(parsed)
