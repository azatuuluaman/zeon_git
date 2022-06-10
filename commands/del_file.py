import os
import sys
from pathlib import Path


def check_del(args):
    if len(args) == 2:
        del_file(args[1])

    elif len(args) == 3:
        print(args[2])
        del_file(args[2])


def del_file(args):
    if len(args) != 2:
        print('Укажите путь до файла')
        exit(0)

    file_name = Path(args[1]).name

    file_path = f'{os.getcwd()}/.zeon_fs/{file_name}'
    print(file_path)

    if not Path(file_name).exists():
        print('Такой файл не существует')
        exit(0)

    os.remove(file_path)


if __name__ == '__main__':
    args = sys.argv
    del_file(args)
