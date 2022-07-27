# 1) Создать список из названий файлов в hookies
# 2) Отсортировать по алфавитному порядку полученный список
# 3) Запустить файлы в hookies по порядку
# 4) Запусить файлы одновременно, если у них в названии есть знак "@".

# Получил список всего, что есть в папке delete/post  ( ПОКАЗЫВАТЬ ТОЛЬКО ФАЙЛЫ)
import os
import subprocess
import threading

list_hookies_with_dog = []
list_hookies = []


def hookies_list(args):
    files = os.listdir(path=f'/home/umar/Desktop/zeon_git/hookies/{args[1]}/pre')

    # Запуск по порядку
    # for file_name in sorted(files):
    #     PATH = f'/home/umar/Desktop/zeon_git/hookies/{args[1]}/pre/{file_name}'
    #     if os.path.isfile(path=PATH):
    #         if "@" in file_name:
    #             list_hookies_with_dog.append(file_name)
    #         else:
    #             list_hookies.append(file_name)
    #     subprocess.call(f'python3 /home/umar/Desktop/zeon_git/hookies/{args[1]}/pre/{file_name}', shell=True)
    # list_hookies.insert(2, list_hookies_with_dog)

    # Меняю её июль 20
    for file_name in sorted(files):
        PATH = f'/home/umar/Desktop/zeon_git/hookies/{args[1]}/pre/{file_name}'
        if os.path.isfile(path=PATH):
            # list_hookies.append(file_name)
            list_hookies.append(PATH)

    print(list_hookies)
    for i in list_hookies:
        if "@" in i:
            subprocess.run(['python3',i])
            # x = threading.Thread(target=i(), args=(1,))
            # x.start()
            continue
        os.system(f'python3 {i}')

        # subprocess.call(f'python3 /home/umar/Desktop/zeon_git/hookies/{args[1]}/pre/{i}', shell=True)
