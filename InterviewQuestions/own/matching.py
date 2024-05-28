'''
Write code that receives 2 folders, 
checks the csv files in them, 
and for each files with the same name and extention in both folders - 
checks if they have the same structure (number of columns and headers name). 
The code will return a list of matching csv files, and a list of unmatching csv files

noamw@ownbackup.com

1. verify the folders are under current directory, with correct path
2. Get the content of each directory into separate list
3. find equal list values
    for each equal list value:
        is it empty
        compare file names are equal str
        fetch the first row 
        compare the first row for the file with the same file name from other folder
if all requerments are met then append the file name to the list of matching
else append the file name to the list of unmatching
return two lists
print

victoria.gur@gmail.com
'''

from collections import Counter
from contextlib import contextmanager
import os, fnmatch, sys
import difflib


class Error(Exception):
    """Base class for other exceptions"""
    pass

class FolderNotInCurrentDirectory(Error):
    """Raised when the folders are not under current directory"""
    pass

class FolderIsEmpty(Error):
    """Raised when the folders are empty"""
    pass

class NoMatchedFileNames(Error):
    """Raised when the folders doesn't contain files with the same name"""
    pass
class PathDoesNotExist(Error):
    """Raised when the path to folders or folders doesn't exist"""
    pass

folders = ('folder1', 'folder2')
matched_list = []
un_matched_list = []

# A context manager ensures no resources are accidentally left open.
@contextmanager
def opened_w_error(filename, mode="r"):
    try:
        f = open(filename, mode)
    except IOError as err:
        yield None, err
    else:
        try:
            yield f, None
        finally:
            f.close()
pass

def match_csv( folder_name_1,  folder_name_2) -> list[str]:
    # Check wether the folders in current directory or not
    # 1). os.walk is a generator and calling next will get the first result in the form of a 3-tuple (dirpath, dirnames, filenames). 
    # Thus the [1] index returns only the dirnames from that tuple.
    # next(os.walk('.'))[1]
    # 2). Check if one tuple is subset of other  set(folders).issubset(next(os.walk('.'))[1])
    try:
        if not set(folders).issubset(next(os.walk('.'))[1]):
            raise FolderNotInCurrentDirectory
    except FolderNotInCurrentDirectory:
        print("Folders not found, please provide valid path")
        print()
    # List containing the names of the entries in the directory given by path. 
    # The list is in arbitrary order.
    list1 = os.listdir(folder_name_1)
    list2 = os.listdir(folder_name_2)
    # Check the folders contain files - not empty
    try:
        if not list1 or not list2:
            raise FolderIsEmpty
    except FolderIsEmpty:
        print("Folders not found, please provide valid path")
        print()
    # list all the matched file names from two folders
    matched_name_lst =  set(list1).intersection(list2)
    try:
        if not matched_name_lst:
            raise NoMatchedFileNames
    except NoMatchedFileNames:
        print("There is no matched filenames in the folders")
        print()
    # For each file in he matchedlist, check the file is not empty and fetch the first line 
    # To safley open huge files with is used reading by lines
    # Can be changed to nested for loops, but for readability left as two separate func call
    for file_name in (list(set(list1).intersection(list2))):
        line_to_list_1 = get_headers_row(folder_name_1, file_name)
        line_to_list_2 = get_headers_row(folder_name_2, file_name)
        # compare two unordered lists using Counter a dict subclass for counting hashable objects.
        if Counter(line_to_list_1) == Counter(line_to_list_2):
            matched_list.append(file_name)
        else:
            un_matched_list.append(file_name)

    return matched_list, un_matched_list

def get_headers_row(folder_name, file_name) -> list:
    path = os.path.join(folder_name, file_name)
    if not os.stat(path).st_size==0:
        with opened_w_error(path, "r") as (f, err):
            if err:
                print ("IOError:", err)
                return None
            else:
                first_line = f.readline()
                return first_line.split(",")


matched_list, un_matched_list = match_csv( folders[0],  folders[1]) 

print('The matched list: ', matched_list)
print('The un matched list: ', un_matched_list)
