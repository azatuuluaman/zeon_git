import sys

from commands.add_file import add_file, check_add
# from commands.del_file import check_del
from commands.del_file import del_file
from commands.hash_file import hash_file
from commands.init_fs import init_fs
from commands.list_files import list_files

import os
from pathlib import Path

# way = os.getcwd()
# dir_name = ".zeon_git"
#
# while not os.path.exists(f"{way}/{dir_name}"):
#     way = Path(way).parent
#     way2 = str(way)
#     if len(way2) == 1:
#         print('File not found')
#         exit(0)
# print(f"{'File found in'}: {way}")

# while not os.path.exists(f"{way}/{dir_name}"):
#     way = Path(way).parent
# print(f"{'File found in'}: {way}")


args = sys.argv

if __name__ == "__main__":

    if args[1] == "list":
        """
        Показывает всё содержимое директории .zeon_git 
        """
        if not len(args) <= 2:
            exit(0)
        print('list worked')
        list_files()

    if args[1] == "init":
        if not len(args) <= 2:
            exit(0)
        init_fs()

    if args[1] == "add":
        check_add(args)

    if args[1] == 'del':
        del_file(args)

    if args[1] == "hash":
        hash_file(args)