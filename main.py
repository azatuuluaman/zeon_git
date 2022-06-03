import os
import sys

args = sys.argv

if args[1] == 'init':
    print('Вызвали инит')
    os.system("python3 init_fs.py")

if args[1] == 'add':
    print('Вызвали add')
    os.system(f"{'python add_file.py'} {args[2]}")

if args[1] == 'del':
    print('Вызвали del')
    os.system(f"{'python del_file.py'} {args[2]}")

if args[1] == 'list':
    print('Вызвали list')
    os.system("python list_files.py")
