import shutil
import sys
from pathlib import Path

args = sys.argv

if len(args) != 2:
    print('Укажите путь до файла')
    exit(0)

if not Path(args[1]).is_file():
    print('Такой файл не существует')
    exit(0)

file_name = Path(args[1]).name

path = '.zeon_fs2/' + file_name

if Path(path).is_file():
    print('Такой файл уже присутсвует')
    exit(0)

shutil.copyfile(args[1], path)
