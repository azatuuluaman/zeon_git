import os
import sys
import zipfile

args = sys.argv
BASE_DIR = '.zeon_git'


def create(args):
    """
    Архивация содержимого с .zeon_git в директорию snapshot
    Команда для терминала: vs create something
    """

    if len(args) > 2:
        PATH_TO = zipfile.ZipFile(f"/home/umar/Desktop/zeon_git/snapshot/{args[2]}.zip", 'w')
        # PATH_TO = zipfile.ZipFile(f"snapshot/{args[2]}.zip", 'w')
        for folder, subfolders, files in os.walk(BASE_DIR):
            for file in files:
                with open(os.path.join(folder, file), 'a') as f:
                    PATH_TO.write(os.path.join(folder, file))

        print('Snapshot add successful')
        PATH_TO.close()
    else:
        print('Enter a name for zip file')


if __name__ == '__main__':
    create(args[2])
