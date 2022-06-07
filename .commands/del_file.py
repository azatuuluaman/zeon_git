import os
import sys
from pathlib import Path
from commands import check_command


def del_file(args):
    file_name = Path(args[1]).name
    file_path = f'{os.getcwd()}.zeon_fs2/{file_name}'

    check_command(args)
    os.remove(file_path)


if __name__ == '__main__':
    args = sys.argv
    del_file(args)
