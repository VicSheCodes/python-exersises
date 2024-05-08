'''
line.split()[0]: After splitting the line, [0] is used to retrieve the first element from the resulting list of
substrings. This corresponds to the first "word" or substring in the line, which is assumed to be the timestamp
in this case.
'''
from pathlib import Path

log_file = Path('C:\\Users\\Cass\\PycharmProjects\\exersises\\SP\\Generators', 'example.log')


def parse_log_file():
    try:
        with open(log_file, 'r') as file:
            timestamp = (line.split()[0:2] for line in file)
            yield from timestamp
    except FileNotFoundError:
        print(f"File '{log_file}' not found.")
    except Exception as e:
        print(f"Error occurred: {e}")
        return None


def test_parse_log_file():
    print()
    print(*(parse_log_file()))

