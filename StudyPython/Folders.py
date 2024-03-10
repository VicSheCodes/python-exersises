import os

folders = set(['folder1', 'folder2', 'folder3'])

def find_folders():
    if not os.path.exists('folder1'):
        os.makedirs('folder1')
    if not os.path.exists('folder2'):
        os.mkdir('folder2')

    if not folders.issubset(next(os.walk('.'))[1]):
        print("Not all folders are present")
        print(folders.difference(next(os.walk('.'))[1]))

    list_of_files_in_folder1 = set(os.listdir('folder1'))
    list_of_files_in_folder2 = set(os.listdir('folder2'))

    common_files = list_of_files_in_folder1.intersection(list_of_files_in_folder2)
    print(f"Common files in folder1: {common_files}")

if __name__ == '__main__':
    find_folders()
