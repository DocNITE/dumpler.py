import subprocess
import sys
import zipfile
import os
from datetime import date

ARCHIVE_FILE_DEF = ".zip"
SQL_FILE_DEF = ".sql"

db_name = "null"
output_path = "null"
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

def dump_path(path):
    return path + SQL_FILE_DEF

def main():
    # global vars
    global db_name
    global output_path
    # do staff
    do_cmd()
    db_name = sys.argv[len(sys.argv)-2]
    output_path = sys.argv[len(sys.argv)-1]
    # local vars
    current_date = date.today()

    print("Dumping database...")
    return_code = subprocess.call(["pg_dump", 
                                   "-h", db_ipaddr, 
                                   "-p", db_port, 
                                   "-U", db_user, 
                                   "-d", db_name, 
                                   "-f", dump_path(output_path)])

    if (return_code != 0):
        print("ERROR: Something wrong...")
        return False
    else:
        print("Done! Dump file '" + dump_path(output_path) + "' successfuly created!")

    arc_name = output_path + "." + str(current_date) + ARCHIVE_FILE_DEF

    print("Packing into '" + arc_name + "'...")
    with zipfile.ZipFile(arc_name, 'w') as zipf:
            zipf.write(dump_path(output_path))

    print("Archive file created!")

    if os.path.exists(dump_path(output_path)):
        os.remove(dump_path(output_path))
main()
