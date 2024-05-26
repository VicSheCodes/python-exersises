import os
from pathlib import Path

word = "in"
filename = Path(r"C:\Users\Cass\PycharmProjects\exersises\SP\FilesManipulation\DataFiles\December\Poetry\LordByron.txt")


def find_word_in_file(path, word):

    folder_path = path.parent
    for file_name in folder_path.iterdir():
        print(f"\n File: {file_name}")
        with open(file_name, 'r') as file:

            lines = file.readlines()
            for line_number, line in enumerate(lines):
                if word in line:
                    print(f"\n {line_number}: {line}")


if __name__ == "__main__":
    print(os.getcwd())

    find_word_in_file(filename, word)