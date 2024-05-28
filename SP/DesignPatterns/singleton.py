import os
import subprocess
from logging import exception


class ExecuteOtherScriptWithCheckSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def execute_other_script_with_check(self, dirname):
        try:
            if not os.path.exists(dirname):
                print(f"\n Executing os_examples.py")
                subprocess.call(["python", "os_examples.py"])
            else:
                print(f"\n\n Directory {dirname} already exists \n")
        except Exception as e:
            print(f"\n{e}")


if __name__ == "__main__":
    try:
        singleton_instance = ExecuteOtherScriptWithCheckSingleton()
        singleton_instance.execute_other_script_with_check(dirname="OsModuleFromClass")
        singleton_instance.execute_other_script_with_check(dirname="OsModuleFromClass")
    except exception as e:
        print(f"\n {e}")
