import webbrowser


def post_add():
    url = 'https://www.youtube.com/watch?v=_Sn2RYQ5yDw'
    webbrowser.open(url, new=1)
    print('Вызов функции после команды add')


if __name__ == '__main__':
    post_add()
