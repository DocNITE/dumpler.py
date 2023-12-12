import subprocess
import zipfile
import os
import sys

ARCHIVE_FILE_DEF = ".zip"
SQL_FILE_DEF = ".sql"

db_name = "null"
input_path = "null"
db_user = "postgres"
db_ipaddr = "localhost"
db_port = "5432"

def do_cmd():
    # global vars
    global db_user 
    global db_ipaddr 
    global db_port
    # local vars 
    counter = 0
    args_len = len(sys.argv)
    args = sys.argv
    # state
    while counter < args_len:
        match args[counter]:
            case "-h": # IP адресс
                counter += 1
                db_ipaddr = args[counter]
            case "-p": # Port
                counter += 1
                db_port = args[counter]
            case "-U": # DB Пользователь
                counter += 1
                db_user = args[counter]
            case _:
                counter += 1

def main():
    # global vars
    global db_name
    global input_path
    # do staff
    do_cmd()
    db_name = sys.argv[len(sys.argv)-2]
    input_path = sys.argv[len(sys.argv)-1]

    with zipfile.ZipFile(input_path, 'r') as zip:
        # Extract all files from the archive
        zip.extractall()
        print("Files extracted successfully.")

    sql_dump_file = input_path.split(".")[0] + SQL_FILE_DEF

    if os.path.exists(sql_dump_file) == False:
        print("ERROR: File doesn't exist!")
        return False

    return_code = subprocess.call(["psql", 
                                   "-h", db_ipaddr, 
                                   "-p", db_port, 
                                   "-U", db_user, 
                                   "-d", db_name, 
                                   "-f", sql_dump_file])

    if (return_code != 0):
        print("ERROR: Something wrong...")
        return False
    else:
        print("Done! Dump file '" + sql_dump_file + "' successfuly loaded!")

    os.remove(sql_dump_file)
main()