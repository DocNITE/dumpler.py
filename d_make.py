import subprocess
import sys

dbname = sys.argv[1]
output_path = sys.argv[2]

# TODO: Сделать чтение аргументов по этим штукам: -U, -h
# И реализовать линейный счетчик чтения массива аргументов.
# Это поможет сбросить ненужное кол-во записываемых приколов
return_code = subprocess.call(["pg_dump", dbname, ">", output_path])
