import requests
import os.path
import re
try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

bar = "3ecf5d9f4e82b22c5dc5c95e2de39018"

def parse(url):
    url = url.split('//')[-1]
    url = url.replace('/',bar)
    return url


def unparse(url):
    url = url.replace(bar,'/')
    url = "http://"+url
    return url


def check_page_cache(problem):
    path = '/tmp/'+problem+'.html'
    if not os.path.exists(path):
        problem_page = requests.get(unparse(problem))
        html = problem_page.text
        with open(path, 'w') as file:
            file.write(html)

def check_input_output(problem):
    input1 = '/tmp/'+problem+'1.in'
    if not os.path.exists(input1):
        check_page_cache(problem)
        path = '/tmp/'+problem+'.html'
        with open(path, 'r') as file:
            parsed_html = BeautifulSoup(file, features='html.parser')

            # problem_title = parsed_html.body.find('div', attrs={'class':'title'}).text
            # print(problem_title)

            inputs = parsed_html.body.find(
                'div',attrs={'class':'input'}).find_all(
                    'div',attrs={'class':re.compile('test-example')})

            if inputs:
                for inp in inputs:
                    print(inp.text)

                outputs = parsed_html.body.find(
                    'div',attrs={'class':'output'}).find('pre')
                print(outputs.text)

            # inputs = parsed_html.body.find(
            #     'div',attrs={'class':'input'}).find_all(
            #         'div',attrs={'class':re.compile('test-example')})

            # if inputs:
            #     for inp in inputs:
            #         print(inp.text)

            #     outputs = parsed_html.body.find(
            #         'div',attrs={'class':'output'}).find('pre')
            #     print(outputs.text)

            # else:
            #     print("MODELO ANTIGO")
            #     delimiter = '\n'
            #     inputs = parsed_html.body.find(
            #         'div',attrs={'class':'input'}).find('pre')
            #     for line in inputs.find_all('br'):
            #         line.replaceWith(delimiter)
            #     print(inputs.text)
            #     outputs = parsed_html.body.find(
            #         'div',attrs={'class':'output'}).find('pre')
            #     for line in outputs.find_all('br'):
            #         line.replaceWith(delimiter)
            #     print(outputs.text)

if __name__ == '__main__':
    # just for testing
    # url = input()
    url = "https://codeforces.com/gym/101021/problem/1"
    parsed = parse(url)
    # print(f"Parsed {parsed}")
    check_input_output(parsed)
