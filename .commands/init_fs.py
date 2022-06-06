import os.path
import sys
from pathlib import Path


def init_fs(args):
    if not len(args) < 2:
        exit(0)

    dir = ".zeon_fs3"

    path = 'zeon_fs2/' + dir

    if not Path(path).is_dir():
        os.makedirs('.zeon_fs3')
        exit(0)


if __name__ == "__main__":
    args = sys.argv
    init_fs(args)
