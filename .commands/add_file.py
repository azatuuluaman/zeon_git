import os
import shutil
import sys
from pathlib import Path
from commands import check_command

args = sys.argv


def add_file(args):
    file_name = Path(args[1]).name
    path = os.getcwd()
    file_path = os.path.join(path, args[0])

    check_command(args)
    dpath = f'.zeon_fs2/{file_name}'
    shutil.copyfile(file_path, dpath)


if __name__ == '__main__':
    args = sys.argv
    add_file(args)
