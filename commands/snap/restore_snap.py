import os.path
import shutil
import sys
import zipfile

PATH_OLD_GIT = '/home/umar/Desktop/zeon_git/.zeon_git'
args = sys.argv
KUDA = 'temporary_name_snapshote'
OTKUDA = '/home/umar/Desktop/zeon_git/snapshot/'


def restore_snap(args):
    """
    Разархивация snapshote -> zip.file -> ( ЕЩЁ УКАЗАТЬ ФАЙЛ?????)  в .zeon_git
    Команда для терминала:  vs restore
    """
    otkuda_zip = zipfile.ZipFile(f"{OTKUDA}{args[2]}.zip")
    otkuda_zip.extractall(KUDA)
    otkuda_zip.close()

    replace_restore()


def replace_restore():
    if os.path.isdir(KUDA) and not os.path.isdir(PATH_OLD_GIT):
        os.rename(f'{KUDA}/.zeon_git', '.zeon_git')
        print('Процесс восстановления произошел успешно')
        return
    shutil.rmtree(PATH_OLD_GIT)
    os.rename(f'{KUDA}/.zeon_git', '.zeon_git')
    os.rmdir(KUDA)   # ОСТАЁТСЯ ПУСТАЯ ПАПКА С ВРЕМЕННЫМ НАЗВАНИЕМ . НУЖНО ИСПРАВИТЬ
    print('Процесс замены произошел успешно')


if __name__ == '__main__':
    restore_snap(args)

