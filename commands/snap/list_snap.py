import os
import sys
import zipfile

args = sys.argv


def list_snap(args):
    if len(args) == 2:
        print(os.listdir('/home/umar/Desktop/zeon_git/snapshot'))
    elif len(args) == 3:
        archive = f"/home/umar/Desktop/zeon_git/snapshot/{args[2]}.zip"
        # ---------------Метод ZipFile.namelist() возвращает список членов архива по имени.
        with zipfile.ZipFile(archive) as zf:
            print(f"Список членов архива по имени в {args[2]}.zip:")
            for name in zf.namelist():
                print(name)


if __name__ == "__main__":
    list_snap(args)
