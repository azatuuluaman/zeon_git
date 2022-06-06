import os
import sys
from pathlib import Path


def del_file(args):
    if len(args) != 2:
        print("Укажите 1 адрес файла для удаления")
        exit(0)

    file_name = Path(args[1]).name
    file_path = f'../.zeon_fs2/{file_name}'

    if not Path(file_path).exists():
        print('Такой файл не существует')
        exit(0)

    os.remove(file_path)


if __name__ == '__main__':
    args = sys.argv
    del_file(args)
