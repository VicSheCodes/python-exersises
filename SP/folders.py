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


folder_name = 'Data_files'


def get_size_of_files_in_folder(folder_name):
    folder_path = os.path.join(os.getcwd(), folder_name)
    file_size = 0
    for dirpath, _, filenames in os.walk(folder_path):
        for filename in filenames:
            file_size += os.path.getsize(os.path.join(dirpath, filename))
    return file_size

def test_get_size_of_files_in_folder():
    assert get_size_of_files_in_folder('Data_files') == 2010

if __name__ == '__main__':
    find_folders()
    print(get_size_of_files_in_folder(folder_name))
