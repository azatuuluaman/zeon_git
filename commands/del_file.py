import os
import shutil
import sys

from commands.hash_file import hash_file

args = sys.argv


# INDEX_CONTENT = f"{args[3]}:{hash_file(args)}"
# PATH_FILE = (INDEX_CONTENT.split(':')[0])


def del_file(args):
    data = []
    # if os.path.isfile(args[2]):
    #     os.remove(args[2])
    #     print(f"Файл по адресу {args[2]} удален")
    # elif os.path.isdir(args[2]):
    #     shutil.rmtree(args[2])
    #     print(f"Папка по адресу {args[2]} удален")
    with open (".zeon_git/index.txt", "r") as file:
        for i in file.readlines():
            if args[2] not in i:
                data.append(i)
    with open (".zeon_git/index.txt", "w") as file2:
        file2.write("".join(data))



# print(INDEX_CONTENT.split(':')[0])       это адрес

if __name__ == '__main__':
    args = sys.argv
    del_file(args)
