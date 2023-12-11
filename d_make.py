import subprocess
import sys
import zipfile
import os
from datetime import date

ARCHIVE_FORMAT_DEF = ".zip"

def main():
    db_name = sys.argv[1]
    output_path = sys.argv[2]

    db_user = "postgres"
    db_ipaddr = "localhost"
    db_port = "5432"

    current_date = date.today()

    # TODO: Сделать чтение аргументов по этим штукам: -U, -h
    # И реализовать линейный счетчик чтения массива аргументов.
    # Это поможет сбросить ненужное кол-во записываемых приколов

    print("Dumping database...")
    return_code = subprocess.call(["pg_dump", "-h", db_ipaddr, "-p", db_port, "-U", db_user, "-d", db_name, "-f", output_path])

    if (return_code != 0):
        print("ERROR: Something wrong...")
        return False
    else:
        print("Done! Dump file '" + output_path + "' successfuly created!")

    arc_name = output_path + "." + str(current_date) + ARCHIVE_FORMAT_DEF

    print("Packing into '" + arc_name + "'...")
    with zipfile.ZipFile(arc_name, 'w') as zipf:
            zipf.write(output_path)

    print("Archive file created!")

    if os.path.exists(output_path):
        os.remove(output_path)
main()
