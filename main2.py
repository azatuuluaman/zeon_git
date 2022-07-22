import sys

from commands.create_snapshot import create
from commands.del_snapshote import del_snap
from commands.list_snap import list_snap
from commands.restore_snapshot import restore_snap

args = sys.argv
# print(f"Этот принт в main.py. Для проверки , что ввёл только что пользователь {args}")
# Команда для терминала: vs create
if __name__ == "__main__":

    if args[1] == 'create':
        create(args)

    if args[1] == "restore":
        restore_snap(args)

    if args[1] == 'del':
        del_snap(args)

    elif args[1] == 'list':
        list_snap()