import sys
from commands.add_file import check_add
from commands.del_file import check_del
from commands.init_fs import init_fs
from commands.list_files import list_files
import os
from pathlib import Path

args = sys.argv


def main(args):
     if args[1] == "list":
        if not len(args) <= 2:
            exit(0)
        list_files()

    if args[1] == "init":
        if not len(args) <= 2:
            exit(0)
        print("Init worked!")
        init_fs()

    if args[1] == "add":
        check_add(args)

    if args[1] == 'del':
        check_del(args)

    dir_name = '.zeon_fs'
    a = os.getcwd()
    find_dir = f"{a}/{dir_name}"

    if Path(find_dir).exists():
        print('File finded! ')
        exit(0)

# way = os.getcwd()
# print(way)
# way = Path(way).parent
# print(way)
