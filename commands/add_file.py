import os
import shutil
import sys

from commands.hash_file import hash_file
from hookies.add.post.post_add import post_add


args = sys.argv


def check_add(args):
    if len(args) <= 4:
        add_file(args)

    else:
        print('Введите правильную команду')


def add_file(args):
    source = os.path.abspath(args[2])
    path = os.getcwd()
    if len(args) == 4 and args[3] != '/':
        PATH = args[3]
    else:
        PATH = args[2]
    """
    Хеширование  -------------------------------------------------------------------------------------------------
    objects
    """
    PATH_OBJECTS = '.zeon_git/objects'

    destination_hash = f"{path}/.zeon_git/objects/{hash_file(args)}"
    if not hash_file(args) in PATH_OBJECTS:
        shutil.copy(source, destination_hash)

    """
    index ------------------------------------------------------------------------------
    """

    INDEX_CONTENT = f"{PATH}:{hash_file(args)}"

    with open(".zeon_git/index.txt", "r") as file:
        if PATH in file:
            print("Already exists in index.txt")
            exit()

        with open(".zeon_git/index.txt", "a") as myfile2:
            myfile2.write(f"{INDEX_CONTENT} \n")
            print("Uploaded")
            post_add()
        exit()


if __name__ == '__main__':
    args = sys.argv
    add_file(args)
