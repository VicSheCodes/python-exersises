'''
Add Prefix to All Filenames in Folder
Pathlib has many practical uses in Python programming.
One of them is changing the prefixes of all the files contained in a folder.
This lesson teaches you how to do that.
'''

from pathlib import Path


def test_change_prefix_to_all_files_in_folder():
    folder_path = Path(r"C:\Users\Cass\PycharmProjects\exersises\SP\FilesManipulation\DataFiles\FoldersToRename")
    for item in folder_path.iterdir():
        print(f" file.name: {item.name} file.stem {item.stem} file.is_file {item.is_file()}")


def test_create_directories_to_rename():
    for i in range(5):
        folder_path = Path(
            r"C:\Users\Cass\PycharmProjects\exersises\SP\FilesManipulation\DataFiles\FoldersToRename\Folder_" + str(i))
        folder_path.mkdir(parents=True, exist_ok=True)
        print(folder_path.is_dir())


def test_create_files_in_each_directory():
    folder_path = Path(r"\Users\Cass\PycharmProjects\exersises\SP\FilesManipulation\DataFiles\FoldersToRename")
    for item in folder_path.iterdir():
        if item.is_dir():
            file_name = "file_"+item.stem[-1]+".txt"
            file_path = item / file_name
            with open(file_path, "w") as f:
                f.write("This is a test!")
                print(file_path)


def test_delete_files_in_each_directory():
    folder_path = Path(r"\Users\Cass\PycharmProjects\exersises\SP\FilesManipulation\DataFiles\FoldersToRename")
    for item in folder_path.iterdir():
        if item.is_dir():
            for file_path in item.iterdir():
                if file_path.is_file():
                    print(file_path.name)
                    file_path.unlink()
