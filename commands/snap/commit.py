import sys
import zipfile

args = sys.argv
PATH_FROM = '/home/umar/Desktop/zeon_git/temp_dir_checkout'


def commit(args):
    """
    Добавляет в зип в снапшоте указанный файл
    vs commit snapshot file_path file_in_snapshot
    0    1       2       3           4
    vs commit (zip name)
    """

    kuda = zipfile.ZipFile(f"/home/umar/Desktop/zeon_git/snapshot/{args[2]}.zip", 'w')
    kuda.write(f"/home/umar/Desktop/zeon_git/temp_dir_checkout/.zeon_git/objects/{args[3]}",
               compress_type=zipfile.ZIP_DEFLATED)
    kuda.close()



if __name__ == "__main__":
    commit(args)
