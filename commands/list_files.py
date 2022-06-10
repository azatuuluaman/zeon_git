import os
import sys


def list_files(*args):
    path = os.getcwd()
    dir_name = '.zeon_fs'
    file_path = os.path.join(path, dir_name)

    dir_files = os.listdir(file_path)

    print('Files: ', len(dir_files))

    for i in dir_files:
        print(i)


if __name__ == "__main__":
    args = sys.argv
    if not len(args) < 2:
        exit(0)
    list_files(sys.argv)
