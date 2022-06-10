import os.path
import sys
from pathlib import Path


def init_fs():

    path = 'zeon_fs2/.zeon_fs'

    print(os.getcwd())

    if not Path(path).is_dir():
        os.makedirs('.zeon_fs')
        exit(0)


if __name__ == "__main__":

    args = sys.argv
    if not len(args) < 2:
        exit(0)
    init_fs()
