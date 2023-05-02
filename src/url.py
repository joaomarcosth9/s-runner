from os.path import exists
import requests

bar = "___s-runner___"  # what will replace the '/' character in URL parsing
s_runner_working_directory = "/tmp/s-runner/"


def parse(url):
    url = url.split('//')[-1]  # remove http(s) protocol
    url = url.replace('/', bar)
    return url


def unparse(url):
    url = url.replace(bar, '/')
    url = "http://" + url  # add http protocol
    return url


def check_page_cache(problem_id, online_judge):
    # To speed up and not having to access the online judge every time,
    # the problem page is cached. This function verifies if it's already
    # cached, and if it isn't, it does.
    full_problem_id = s_runner_working_directory + problem_id
    path = full_problem_id + '.html'
    if not exists(path):
        try:
            problem_page = requests.get(unparse(problem_id))
            if problem_page.status_code != 200:
                raise Exception("Can't reach site URL.")
            html = problem_page.text
            with open(path, 'w') as file:
                file.write(html)
        except Exception as error:
            print(f"Something went wrong while checking {online_judge} page.")
            print(error)
            exit(1)
