import os.path
import sys
from pathlib import Path


def init_fs():
    dir_object = '.zeon_git/objects'
    file_index = '.zeon_git/index.txt'
    if not Path(dir_object).is_dir():
        os.makedirs(dir_object)
        print('Directory objects create')
    if not Path(file_index).is_file():
        Path(file_index).touch()
        print('File index create')


if __name__ == "__main__":

    args = sys.argv
    if not len(args) < 2:
        exit(0)
    init_fs()
