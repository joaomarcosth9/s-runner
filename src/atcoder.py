from os.path import exists
from bs4 import BeautifulSoup


from url import parse, check_page_cache


s_runner_working_directory = "/tmp/s-runner/"


def check_input_output_cache(problem_id):
    # Check if the problem's input and output are cached
    # and if they aren't, it does.
    full_problem_id = s_runner_working_directory + problem_id
    inputfile = full_problem_id + '.input'
    outputfile = full_problem_id + '.output'  # Currently I'm not using the output for nothing.
    if not exists(inputfile) or not exists(outputfile):
        check_page_cache(problem_id, 'atcoder')
        page_path = full_problem_id + '.html'
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
                    for index, inputbox in enumerate(all_input_boxes):
                        with open(full_problem_id + '.in' + str(index), 'w') as inputbox_number_i:
                            inputbox_number_i.write(inputbox)
                    number_of_inputs.write(str(total))
                with open(outputfile, 'w') as real_output_file:
                    for outputbox in all_output_boxes:
                        real_output_file.write(outputbox)

        except Exception as err:
            print("Something went wrong while parsing input/output.")
            print(err)
            exit(1)


if __name__ == '__main__':
    # just for testing
    url = input()
    parsed = parse(url)
    check_input_output_cache(parsed)
