import sys
import zipfile

from termcolor import colored

args = sys.argv
PATH = '/home/umar/Desktop/zeon_git/snapshot/'
PATH_TO = '/home/umar/Desktop/zeon_git/temp_dir_checkout'


def checkout(args):
    """
    Разархивация файла из .zeon_git в временную директорию temp_dir_checkout
    Команда для терминала vs checkout snapshot hash
    """
    archive = f'/home/umar/Desktop/zeon_git/snapshot/{args[2]}.zip'

    object = f".zeon_git/objects/{args[3]}"
    with zipfile.ZipFile(archive, 'r') as zip_file:
        zip_file.extract(object, '/home/umar/Desktop/zeon_git/temp_dir_checkout')

    print(colored(f'{args[3]} -> temp_dir_checkout ', 'green'))


if __name__ == '__main__':
    checkout(args)

# нужно указать не хеш ,а путь который хранится в индексе.
# конфиги джанго прочитать