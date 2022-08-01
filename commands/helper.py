# 1) Создать список из названий файлов в hookies
# 2) Отсортировать по алфавитному порядку полученный список
# 3) Запустить файлы в hookies по порядку
# 4) Запусить файлы одновременно, если у них в названии есть знак "@".

# Получил список всего, что есть в папке delete/post  ( ПОКАЗЫВАТЬ ТОЛЬКО ФАЙЛЫ)
import os
import subprocess

list_hookies_with_dog = []
list_hookies = []


def hookies_list(args):
    files = os.listdir(path=f'/home/umar/Desktop/zeon_git/hookies/{args[1]}/pre')

    for file_name in sorted(files):
        path = f'/home/umar/Desktop/zeon_git/hookies/{args[1]}/pre/{file_name}'
        if os.path.isfile(path=path):
            list_hookies.append(path)

    for i in list_hookies:
        if "@" in i:
            subprocess.run(['python3', i])
            continue
        os.system(f'python3 {i}')
