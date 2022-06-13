import os
import shutil
import sys
from pathlib import Path

# args = sys.argv
#
#
# def check_add(arge


#
#
#
# def add_file(*args):
#     file_name = args
#
#     if not Path(args[2]).exists():
#         print('Такой файл не существует')
#         exit(0)
#
#     path = os.getcwd()
#
#     file_path = os.path.join(path, file_name)  # АДРЕС ФАЙЛА КОТОРОЕ ХОТИМ ДОБАВИТЬ
#
#     dir_path = '.zeon_fs'
#
#     dpath = f'{path}/{dir_path}/{file_name}'  # Адрес куда нужно сохранить, с назваием как нужно сохранить
#
#     shutil.copyfile(file_path, dpath)
#
#
# if __name__ == '__main__':
#     args = sys.argv
#     check_add(args)


args = sys.argv


# def check_add(args):
#     if len(args) == 2:
#         add_file(args[1])
#
#     if len(args) == 4:
#         add_file(args[2], args[3])
#
#     elif len(args) == 3:
#         add_file(args[2])


def add_file(args):
    source = os.path.abspath(args[2])  # Istochnik
    print('Адрес источника: ', source)

    os.makedirs(args[3], exist_ok=True)

    os.getcwd()

    path = os.getcwd()

    destination1 = f"{path}/{args[3]}"
    print("Адрес назначения без имени: ", destination1)

    shutil.copy(source, destination1)


if __name__ == '__main__':
    args = sys.argv
    add_file(args)
