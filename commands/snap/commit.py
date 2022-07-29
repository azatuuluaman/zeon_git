import os
import sys
import zipfile

args = sys.argv
PATH_FROM = '/home/umar/Desktop/zeon_git/temp_dir_checkout'


def commit(args):
    # zip_file_in_snap = f"/home/umar/Desktop/zeon_git/snapshot/{args[2]}.zip"
    # print(f"Zip file in snapshot:  {zip_file_in_snap}")
    replace_b = f"/home/umar/Desktop/snapshot/{args[2]}/.zeon_git/objects/{args[3]}"
    # file_in_zipfile = f"/home/umar/Desktop/snapshot/{args[2]}/.zeon_git/objects/{args[3]}"

    archive = '/home/umar/Desktop/zeon_git/snapshot/archive1.zip'
    zip_file = zipfile.ZipFile(archive)
    zip_file.namelist()

    print(replace_b)

    # ---------------Метод ZipFile.namelist() возвращает список членов архива по имени.
    # with zipfile.ZipFile(archive) as zf:
    #     print(f"Список членов архива по имени в {args[2]}.zip:")
    #     for name in zf.namelist():
    #         print(name)


    # archive = '/home/umar/Desktop/zeon_git/snapshot/archive1.zip'
    #
    # object = f".zeon_git/objects/{args[2]}"
    # with zipfile.ZipFile(archive, 'r') as zip_file:
    #     zip_file.extract(object, '/home/umar/Desktop/zeon_git/temp_dir_checkout')















    # print('Commit work!')
    # path_to = zipfile.ZipFile(f"/home/umar/Desktop/zeon_git/snapshot/{args[2]}.zip", "w")
    #
    #
    # for folder, subfolders, files in os.walk('/.temp_dir_checkout'):
    #     for file in files:
    #         path_to.write(os.path.join(folder, file),
    #                       os.path.relpath(os.path.join(folder, file), '/.temp_dir_checkout'),
    #                       compress_type=zipfile.ZIP_DEFLATED)
    # print('Commit successful')
    # path_to.close()


if __name__ == "__main__":
    commit(args)
