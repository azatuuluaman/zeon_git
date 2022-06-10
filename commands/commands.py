
from pathlib import Path


def check_command(args):
    if len(args) != 2:
        print('Укажите путь до файла')
        exit(0)

    file_name = Path(args[1]).name

    if not Path(file_name).exists():
        print('Такой файл не существует')
        exit(0)
