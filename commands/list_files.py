import sys


def list_files():
    elements = []
    files = {}

    with open(".zeon_git/index.txt", "r") as file:
        for link in file.read().split('\n'):
            elements.append(link.split(':')[0])
        print(elements)

    for element in elements:
        link = files
        for path in element.split('/'):
            if not path in link:
                link[path] = {}
            link = link[path]

    def to_tree(d, c=0):
        for a, b in d.items():
            yield '   '.join('|' for _ in range(c + 1)) + f'---{a}'
            yield from ([] if b is None else to_tree(b, c + 1))

    print('\n'.join(to_tree(files)))


if __name__ == "__main__":
    args = sys.argv
    if not len(args) <= 2:
        exit(0)
    list_files()
