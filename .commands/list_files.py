import os
import sys


def list_files(*args):
    if not len(args) < 2:
        exit(0)

    dir_name = '.zeon_fs2'
    dir_files = os.listdir(dir_name)
    print('Files: ',len(dir_files))

    for i in dir_files:
        print(i)

if __name__ == "__main__":
    args = sys.argv
    list_files(args)
