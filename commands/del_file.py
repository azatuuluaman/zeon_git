import os
import shutil
import sys

args = sys.argv



def del_file(args):
    if os.path.isfile(args[2]):
        os.remove(args[2])
        print(f"Файл по адресу {args[2]} удален")
    elif os.path.isdir(args[2]):
        shutil.rmtree(args[2])
        print(f"Папка по адресу {args[2]} удален")




if __name__ == '__main__':
    args = sys.argv
    del_file(args)
