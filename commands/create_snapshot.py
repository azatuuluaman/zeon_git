import os
import sys
import zipfile

args = sys.argv


def create(args):
    """
    Архивация содержимого с .zeon_git в директорию snapshot
    Команда для терминала: vs create
    """
    # Здесь должен быть адрес куда сохранять и под каким именем, имя указывает пользователь
    PATH_TO = zipfile.ZipFile(f"/home/umar/Desktop/zeon_git/snapshot/{args[2]}.zip", 'w')

    for folder, subfolders, files in os.walk('/home/umar/Desktop/zeon_git/.zeon_git'):
        for file in files:
            PATH_TO.write(os.path.join(folder, file),
                          os.path.relpath(os.path.join(folder, file), '/home/umar/Desktop/zeon_git/.zeon_git'),
                          compress_type=zipfile.ZIP_DEFLATED)
    print('Snapshot add successful')
    PATH_TO.close()


if __name__ == '__main__':
    create(args[2])
