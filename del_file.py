import os
import sys
from pathlib import Path

args = sys.argv

if len(args) != 2:
    print("Укажите 1 адрес файла для удаления")
    exit(0)

file_name = Path(args[1]).name

path = ".zeon_fs2/" + file_name

if not Path(path).is_file():
    print('Такого файла нет')
    exit(0)

os.remove(path)
