"""
Pathlib is a module in Python that provides an object-oriented interface for working with filesystem paths.
It was introduced in Python 3.4 and offers a more intuitive and platform-independent way to manipulate
filesystem paths compared to traditional string-based methods.

Advantages of Pathlib:

Object-oriented approach: Pathlib provides classes to represent filesystem paths as objects,
allowing for cleaner and more readable code.
Platform independence: Pathlib automatically handles differences in path conventions between
operating systems (e.g., Windows, Unix).
Concise syntax: Pathlib methods and properties offer a more concise and expressive way to perform
common filesystem operations.

Basic Pathlib Operations - Creating Paths
How to import pathlib module.
Creating a Path object for a directory.
List all files in the directory using iterdir() method.
How to iterate through the files and rename them by adding a prefix.
"""
import os
from pathlib import Path


def test_create_path_and_list():
    # Creating a Path object for a directory
    folder_path = Path(r"C:\Users\Cass\PycharmProjects\exersises\SP\FilesManipulation\DataFiles\December")
    print(f"\n folder_path {folder_path}")

    # Joining paths using the / operator
    new_path = folder_path / "Income" / "income.txt"
    print(f"\n new_path {new_path}")
    print(f" new_path.name {new_path.name}")  # Output: income.txt
    print(f" new_path.parent {new_path.parent}")  # Output: C:\Users\Cass\PycharmProjects\exersises\SP\FilesManipulation\DataFiles\December\Income
    print(f" new_path.exists() {new_path.exists()}")  # Output: True or False
    print(f" new_path.is_file() {new_path.is_file()}")  # Output: True or False
    print(f" new_path.is_dir() {new_path.is_dir()}")  # Output: True or False
    print(new_path.stem)  # file
    print(new_path.suffix)  # .txt

    # Listing contents of a directory
    for item in folder_path.iterdir():
        print(f" \n files n ame: {item.name}")


# add a prefix to each filename in the folder.

def add_prefix_to_files(folder_path, prefix):
    folder = Path(folder_path)
    for file in folder.iterdir():
        if file.is_file():
            new_name = folder.joinpath(prefix + file.name)
            file.rename(new_name)


# Example usage
def test_add_prefix_to_files():
    folder_path = r"C:\Users\Cass\PycharmProjects\exersises\SP\FilesManipulation\DataFiles\November"
    prefix = "_"
    add_prefix_to_files(folder_path, prefix)


# modify the script to accept a customizable prefix instead of a fixed one.
def add_prefix_to_files_customized(folder_path, prefix):
    folder = Path(folder_path)
    for file in folder.iterdir():
        if file.is_file():
            new_name = folder.joinpath(prefix + file.name)
            if new_name.exists():
                # Handle case where filename already exists
                print(f"Skipping {file.name}, filename already exists.")
            else:
                file.rename(new_name)


# Example usage with customizable prefix
def test_add_prefix_to_files_customized():
    folder_path = r"C:\Users\Cass\PycharmProjects\exersises\SP\FilesManipulation\DataFiles\November"
    user_prefix = input("Enter the prefix to add: ")
    add_prefix_to_files_customized(folder_path, user_prefix)
