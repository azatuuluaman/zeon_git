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
    path = os.getcwd()
    # текущая папка

    file_path = os.path.join(path, args[0])
    # Создаёт новый адрес, добавляет слеш между двумя сигнатурами

    if not Path(file_path).exists():
        """ 
        Есть ли такой файл по данному адресу?
        """
        print('Такой файл не существует')
        exit(0)

    dpath = f'../.zeon_fs2/{file_name}'

    if Path(dpath).exists():
        print('Такой файл уже присутсвует')
        exit(0)

    shutil.copyfile(file_path, dpath)


if __name__ == '__main__':
    args = sys.argv
    add_file(args)
