import os
import shutil
import sys
from pathlib import Path

args = sys.argv


def check_add(args):
    if len(args) == 2:
        add_file(args[1])

    elif len(args) == 3:
        print(args[2])
        add_file(args[2])


def add_file(args):
    file_name = args

    print(file_name)
    if not Path(args).exists():
        print('Такой файл не существует')
        exit(0)

    path = os.getcwd()

    file_path = os.path.join(path, file_name)  # АДРЕС ФАЙЛА КОТОРОЕ ХОТИМ ДОБАВИТЬ

    dir_path = '.zeon_fs'

    dpath = f'{path}/{dir_path}/{file_name}'  # Адрес куда нужно сохранить, с назваием как нужно сохранить

    shutil.copyfile(file_path, dpath)


if __name__ == '__main__':
    args = sys.argv
    check_add(args)
