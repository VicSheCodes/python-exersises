import os

filename = 'text_file.txt'
directory = os.path.dirname(os.getcwd())
filename_path = os.path.join(directory, 'Data_files', 'text_file.txt')


def find_a_file_in_the_directory():
    for root, dirs, files in os.walk(directory):
        if filename in files:
            return os.path.join(root, filename)

    return None


filename_path_2 = find_a_file_in_the_directory()


def read_lines():
    with open(filename_path, 'r') as f:
        for line in f:
            yield line.strip()


def test_read_lines():
    all_lines = [line for line in read_lines()]
    assert all_lines[6] == 'Rising up through the air'

    all_lines = [*read_lines()]
    assert all_lines[6] == 'Rising up through the air'
