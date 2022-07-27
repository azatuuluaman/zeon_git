import os
import sys
import zipfile

args = sys.argv
PATH_FROM = '/home/umar/Desktop/zeon_git/temp_dir_checkout'


def commit(args):
    print('Commit work!', args[2])
    path_to = zipfile.ZipFile(f"/home/umar/Desktop/zeon_git/snapshot/{args[2]}.zip", "w")


    for folder, subfolders, files in os.walk('/.temp_dir_checkout'):
        for file in files:
            path_to.write(os.path.join(folder, file),
                          os.path.relpath(os.path.join(folder, file), '/.temp_dir_checkout'),
                          compress_type=zipfile.ZIP_DEFLATED)
    print('Commit successful')
    path_to.close()


if __name__ == "__main__":
    commit(args)
