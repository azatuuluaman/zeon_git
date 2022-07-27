import os.path
import sys

PATH_OLD_GIT = '/.zeon_git'
PATH_SNAP = '/home/umar/Desktop/zeon_git/snapshot/'
args = sys.argv


def del_snap(args):
    """
    Delete zip file in dir snapshote
    Terminal: vs del name_zip_file
    """

    if os.path.isfile(PATH_SNAP + args[2] + '.zip'):
        os.remove(PATH_SNAP + args[2] + '.zip')
        print(f'File {args[2]} in dir snapshote delete')
    else:
        print('There is no such file')


if __name__ == '__main__':
    del_snap(args)
