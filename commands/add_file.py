import os
import shutil
import sys

from commands.hash_file import hash_file

args = sys.argv


def check_add(args):
    print(args)
    if len(args) <= 4:
        add_file(args)
    else:
        print('Введите правильную команду')


def add_file(args):
    source = os.path.abspath(args[2])
    path = os.getcwd()
    # start_path = f"{path}/{'.zeon_git'}/{args[3]}"
    # finis_path = f"{start_path}{args[2]}"
    # print("start_path", start_path)
    # print("finish_path",finis_path)
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
        exit()

    """
    ----------------------------------------------------------------------------------
    """

    # if args[-1][-1] == "/":
    #     os.makedirs(start_path, exist_ok=True)
    #     shutil.copyfile(source, finis_path)
    #     print(f"Скопировали файл {args[2]} в директорию {finis_path}")
    #
    # elif args[-1][-1] != "/":
    #     razdel = (args[3].split("/"))
    #     razdel2 = (args[3].split("/"))
    #     print(f"Новое название для файла {razdel2[-1]}")
    #
    #     razdel.pop()
    #
    #     adres = "/".join(razdel)
    #
    #     kuda = f"{path}/{'.zeon_git'}/{adres}"
    #
    #     print(f"Адрес назначения {kuda}")
    #     os.makedirs(kuda, exist_ok=True)
    #     shutil.copy(source, f"{kuda}/{razdel2[-1]}")


if __name__ == '__main__':
    args = sys.argv
    add_file(args)
