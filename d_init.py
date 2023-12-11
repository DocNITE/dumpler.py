import os
import sys
import subprocess

def main():
    current_path = os.environ.get('PATH')
    psql_path = sys.argv[1]
    d_path = sys.argv[2]

    # maybe there is no need use d_make and d_load
    if (os.path.exists(psql_path) == False) or (os.path.exists(d_path) == False):
        print("Paths doesn't exist. Check valid directory paths for `psql.exe` and `d_make.exe`, `d_load.exe`")
        return False

    if current_path:
        psql_path_value = f'{current_path};{psql_path};{d_path}'  # Добавление нового пути в конец
    else:
        psql_path_value = psql_path

    command = f'setx PATH "{psql_path_value}"'
    subprocess.call(command, shell=True)
    updated_path = os.environ.get('PATH')
    print(updated_path)
main()