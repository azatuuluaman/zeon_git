import sys

args = sys.argv


def del_file(args):
    data = []
    print('Del rabotaet')
    with open(".zeon_git/index.txt", "r") as file:
        for i in file.readlines():
            if args[2] not in i:
                data.append(i)
    with open(".zeon_git/index.txt", "w") as file2:
        file2.write("".join(data))


if __name__ == '__main__':
    args = sys.argv
    del_file(args)
