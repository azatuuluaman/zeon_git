import sys
import zipfile

from termcolor import colored

args = sys.argv
PATH = '/home/umar/Desktop/zeon_git/snapshot/'
PATH_TO = '/home/umar/Desktop/zeon_git/temp_dir_checkout'


def checkout(args):
    """
    Разархивация содержимого из указанного файла с каталога snapshot в временную директорию temp_dir_checkout
    Команда для терминала vs checkout (файл внутри каталога snapshot)

    Разархивация snapshote -> file.zip -> file
    """

    path_from = f"{PATH}{args[2]}.zip"
    from_zip = zipfile.ZipFile(path_from)
    from_zip.extractall(PATH_TO)
    from_zip.close()
    print(colored('Checkout work!', 'green'))


if __name__ == '__main__':
    checkout(args)


