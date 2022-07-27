import sys

from commands.snap.checkout_snap import checkout
from commands.snap.commit import commit
from commands.snap.create_snap import create
from commands.snap.del_snap import del_snap
from commands.snap.list_snap import list_snap
from commands.snap.restore_snap import restore_snap

args = sys.argv
# print(f"Этот принт в main.py. Для проверки , что ввёл только что пользователь {args}")
# Команда для терминала: vs create
if __name__ == "__main__":

    if len(args) == 1:
        print('Введите правильную команду для работы с snapshote: \n - vs create something \n - vs restore something \n - vs del something\n - vs list')
        exit(0)

    if args[1] == 'create':
        create(args)

    if args[1] == "restore":
        restore_snap(args)

    if args[1] == 'del':
        del_snap(args)

    elif args[1] == 'list':
        list_snap()

    elif args[1] == 'checkout':
        checkout(args)

    elif args[1] == 'commit':
        commit(args)

