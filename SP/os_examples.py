import os
import subprocess
from logging import exception


def create_directory_and_manage_files():
    """
    os.mkdir() function call you provided will attempt to create a directory named "Os_module"
    with full permissions (0o777), and if it already exists, it will not raise an error
    (exist_ok=True). Additionally, if any of the parent directories leading up to "Os_module"
    do not exist, it will create them (parents=True).

    """
    print(f"\n Current working directory: {os.getcwd()}")
    os.makedirs("OsModule", exist_ok=True, mode=0o777)
    if os.path.exists("OsModule"):
        print(f"\n Directory 'OsModule' created successfully")
    os.chdir("OsModule")
    print(f"\n Current working directory: {os.getcwd()}")
    print(f"\n Absolute path {os.path.abspath('.')}")
    with open("os_examples.py", 'w') as file:
        file.write("import os\n\n\n"
                   "def show_current_dir():\n"
                   "\tprint(Hello {os.getcwd})\n")
    with open("os_examples.py", 'r') as file:
        f = file.read()
        print(f"\n\n {f}")


def find_file(filename, search_path):
    if os.path.exists(search_path):
        for root, dirs, files in os.walk(search_path):
            if filename in files:
                return os.path.join(root, filename)
        else:
            return None


def up_to_parent_directory():
    os.chdir(os.path.dirname(os.path.abspath('.')))
    print(f"\n Current working directory: {os.getcwd()}")


def execute_other_script_with_flag():
    up_to_parent_directory()
    result = None
    if not os.path.exists("flag.txt"):
        print(f"\n Executing dictionaries.py")
        path = find_file("dictionaries.py", "..")
        if not path:
            print(f"\n Could not find dictionaries.py")
        else:
            result = subprocess.run(["python", path], capture_output=True, text=True)
        with open("flag.txt", 'w') as file:
            file.write("flag")
    return result


def execute_other_script_with_check_singleton(dirname='OsModule'):
    _instance = None
    if not _instance:
        _instance = True
        try:
            if not os.path.exists(dirname):
                print(f"\n Executing os_examples.py")
                result = subprocess.run(["python", "os_examples.py"], capture_output=True, text=True)
            else:
                print(f"\n Directory {dirname} already exists")
        except exception as e:
            print(f"\n {e}")
    return result


if __name__ == "__main__":
    try:
        print(create_directory_and_manage_files())
        print(execute_other_script_with_flag())
    except exception as e:
        print(f"\n {e}")
