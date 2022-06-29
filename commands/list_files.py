import os
import sys
import os.path


def list_files():
    for address, dirs, files in os.walk('.zeon_git'):
        print(address,dirs,files)

        for name in files:
            print(os.path.join(address, name))

if __name__ == "__main__":
    args = sys.argv
    if not len(args) < 2:
        exit(0)
    list_files()

