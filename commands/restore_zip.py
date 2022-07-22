import os.path
import shutil
import zipfile

PATH_OLD_GIT = '/home/umar/Desktop/zeon_git/.zeon_git'


def restore_zip():
    """
    Разархивация содержимого с ZIP в переменную с временным названием temporary_name
    Команда для терминала: fs restore
    """
    fantasy_zip = zipfile.ZipFile('/home/umar/Desktop/zeon_git/archive.zip')
    fantasy_zip.extractall('/home/umar/Desktop/zeon_git/temporary_name')

    # print("Разархивация в директорию temporary_name")
    fantasy_zip.close()
    check_restore()


def check_restore():
    if os.path.isdir('temporary_name') and not os.path.isdir(PATH_OLD_GIT):
        os.rename('temporary_name', '.zeon_git')
        print('Процесс восстановления произошел успешно')
        return
    shutil.rmtree(PATH_OLD_GIT)
    os.rename('temporary_name', '.zeon_git')
    print('Процесс замены произошел успешно')


if __name__ == '__main__':
    restore_zip()
