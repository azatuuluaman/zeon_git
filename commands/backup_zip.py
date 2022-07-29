import os
import zipfile


def backup_zip():
    """
    Архивация содержимого с .zeon_git в archive1.zip
    Команда для терминала:  fs backup
    """
    fantasy_zip = zipfile.ZipFile('/home/umar/Desktop/zeon_git/archive.zip', 'w')

    for folder, subfolders, files in os.walk('/home/umar/Desktop/zeon_git/.zeon_git'):
        for file in files:
            fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder, file),
                                                                          '/home/umar/Desktop/zeon_git/.zeon_git'),
                              compress_type=zipfile.ZIP_DEFLATED)
    print('Архивация содержимого с .zeon_git в archive1.zip succesful')
    fantasy_zip.printdir()
    fantasy_zip.close()


if __name__ == '__main__':
    backup_zip()
