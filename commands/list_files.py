import os
import sys


def list_files(*args):
    if not len(args) < 2:
        exit(0)

    dir_name = '../.zeon_fs2'
    dir_files = os.listdir(dir_name)

    files = []

    for file in dir_files:
        if os.path.isfile(file): files.append(file)

    str_files = " ".join(files)
    print('Files:', len(files))
    print(str_files)


if __name__ == "__main__":
    args = sys.argv
    list_files(args)

# вызов функции ( сигнатура принимает
