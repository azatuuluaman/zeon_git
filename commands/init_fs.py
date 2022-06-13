import os.path
import pathlib
import sys
from pathlib import Path


def init_fs():
    path = 'zeon_fs2/.zeon_fs'

    if not Path(path).is_dir():
        os.makedirs('.zeon_fs')
        exit(0)


if __name__ == "__main__":

    args = sys.argv
    if not len(args) < 2:
        exit(0)
    init_fs()


# def init_fs(args):
#     """
#     Создает директории внутри дирекиориииииии
#     :param args:
#     :return:
#     """
#
#     print(type(args[2]))
#     pathlib.Path(args[2]).mkdir(parents=True, exist_ok=True)
#
#
# if __name__ == "__main__":
#
#     args = sys.argv
#     if not len(args) < 2:
#         exit(0)
#     init_fs(args)


