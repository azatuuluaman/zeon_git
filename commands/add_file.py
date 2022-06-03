import os
import shutil
import sys
from pathlib import Path

args = sys.argv


def add_file(args):
    if len(args) != 2:
        print('Укажите путь до файла')
        exit(0)

    file_name = Path(args[1]).name

    path = '../.zeon_fs2/'
    print(os.listdir(path))
    print(args[1])

    if not Path(args[1]).is_file():
        print('Такой файл не существует')
        exit(0)

    if Path(path).is_file():
        print('Такой файл уже присутсвует')
        exit(0)

    shutil.copyfile(args[1], path)


if __name__ == '__main__':
    args = sys.argv
    add_file(args)
