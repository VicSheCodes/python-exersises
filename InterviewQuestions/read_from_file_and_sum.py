''''
read lines from file path, each line convert contain a number,
square up and then accumulate all squares to sum and return
'''
import os

start_path = os.path.dirname(os.getcwd())


def find_file_path(start_path, file_name):
    for root, dirs, files in os.walk(start_path):
        if file_name in files:
            return os.path.join(root, file_name)
    return None


def read_from_file_sqr_and_sum(file_path):
    with open(file_path, 'r') as file:
        file_to_list = file.readlines()
        print("\nfile after read lines: ", file)
        print("\nfile_to_list after reade lineS: ", file_to_list, type(file_to_list))

        file.seek(0)
        line = file.readline()
        print("\nread line: ", line, type(line))

        file.seek(0)
        file_to_str = ''.join(line.rstrip('\n') for line in file)
        print("\nfile_to_str after file read : ", file_to_str, type(file_to_str))


def generate_from_huge_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield (int(line.rstrip()) ** 2)


if __name__ == '__main__':
    abs_path = find_file_path(start_path, 'numbers')
    read_from_file_sqr_and_sum(abs_path)
    print("\npath: ", abs_path)
    result = sum(num for num in generate_from_huge_file(abs_path))
    print(result)
