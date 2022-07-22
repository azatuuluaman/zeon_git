import os.path
import shutil
import sys
import zipfile

PATH_OLD_GIT = '/home/umar/Desktop/zeon_git/.zeon_git'

args = sys.argv


def restore_snap(args):
    """
    Разархивация содержимого из указанного файла с каталога snapshot
    Команда для терминала: vs restore
    """
    fantasy_zip = zipfile.ZipFile(f'/home/umar/Desktop/zeon_git/snapshot/{args[2]}.zip')
    fantasy_zip.extractall('/home/umar/Desktop/zeon_git/temporary_name_snapshote')

    print(f"Разархивация {args[2]} в директорию temporary_name_snapshote")
    fantasy_zip.close()
    check_restore()


def check_restore():
    if os.path.isdir('temporary_name_snapshote') and not os.path.isdir(PATH_OLD_GIT):
        os.rename('temporary_name_snapshote', '.zeon_git')
        print('Процесс восстановления произошел успешно')
        return
    shutil.rmtree(PATH_OLD_GIT)
    os.rename('temporary_name_snapshote', '.zeon_git')
    print('Процесс замены произошел успешно')


if __name__ == '__main__':
    restore_snap(args)
