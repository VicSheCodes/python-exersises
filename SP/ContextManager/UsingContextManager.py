import os
import tempfile


def working_with_files():
    current_directory = os.getcwd()
    print("Current Working Directory:", current_directory)

    for root, directories, files in os.walk(current_directory):
        print(f"Current Directory: {root}")

        # Print subdirectories
        print("Subdirectories:", directories)

        # Print filenames
        print("Files:", files)

        print("\n")

    with open("test.txt", 'w') as test_file:
        test_file.write("This is a test!\n")

    with open("test.txt", 'r') as test_file:
        content = test_file.read()

    print(content)


if __name__ == '__main__':
    working_with_files()
