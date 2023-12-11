import subprocess
import zipfile
import os
import sys

#TODO: Разбиение путей и загрузку архива по его первому имени.

ARCHIVE_FORMAT_DEF = ".zip"

db_name = sys.argv[1]
input_path = sys.argv[2]

db_user = "postgres"
db_ipaddr = "localhost"
db_port = "5432"

with zipfile.ZipFile(input_path, 'r') as zip:
    # Extract all files from the archive
    zip.extractall()
    print("Files extracted successfully.")

return_code = subprocess.call(["psql", "-h", db_ipaddr, "-p", db_port, "-U", db_user, "-d", db_name, "-f", input_path])

if (return_code != 0):
    print("ERROR: Something wrong...")
else:
    print("Done! Dump file '" + input_path + "' successfuly loaded!")
"""

# Splitting a string using a hyphen as the delimiter
string = "Alice-Bob-Charlie"
result = string.split("-")  
print(result)


# Specify the path of the ZIP archive file
zip_path = 'path/to/archive.zip'

# Open the ZIP archive
with zipfile.ZipFile(zip_path, 'r') as zip:
    # Extract all files from the archive
    zip.extractall()
    print("Files extracted successfully.")
"""