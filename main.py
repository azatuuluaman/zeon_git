import sys
import threading

from commands.add_file import check_add
from commands.backup_zip import backup_zip
from commands.del_file import del_file
from commands.hash_file import hash_file
from commands.helper import hookies_list
from commands.init_fs import init_fs
from commands.list_files import list_files
from commands.restore_zip import restore_zip

from hookies.add.post.post_add import post_add
from hookies.add.pre.pre_add import pre_add
from hookies.delete.post.post_del import post_del

args = sys.argv
# print(f"Этот принт в main.py. Для проверки , что ввёл только что пользователь {args}")

if __name__ == "__main__":

    if len(args) == 1:
        print(
            'Введите правильную команду: \n - fs list \n - fs init \n - fs add something \n - fs delete something \n - fs hash something \n - fs backup something')
        exit(0)

    if args[1] == "list":
        if not len(args) <= 2:
            exit(0)
        list_files()
        hookies_list(args)

    if args[1] == "init":
        if not len(args) <= 2:
            exit(0)
        init_fs()

    if args[1] == "add":
        x = threading.Thread(target=pre_add(), args=(1,))
        check_add(args)
        # post_add()

    if args[1] == 'delete':
        del_file(args)
        post_del()

    if args[1] == "hash":
        hash_file(args)

    if args[1] == "backup":
        backup_zip()

    if args[1] == 'restore':
        restore_zip()
