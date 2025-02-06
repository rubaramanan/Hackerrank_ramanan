l = []


def ins(value, index):
    l.insert(index, value)


def app(value, index=None):
    l.append(value)


def rem(value, index=None):
    l.remove(value)


def pri(value=None, index=None):
    print(l)


def sor(value=None, index=None):
    l.sort()


def po(value=None, index=None):
    l.pop()


def rev(value=None, index=None):
    l.reverse()


def get_command(command: str):
    key = command.split()
    com = key[0]
    index = None
    value = None

    if len(key) == 3:
        index = int(key[1])
        value = int(key[2])
    if len(key) == 2:
        value = int(key[1])
    return com, value, index


dic = {
    'insert': ins,
    'append': app,
    'remove': rem,
    'print': pri,
    'sort': sor,
    'pop': po,
    'reverse': rev

}
if __name__ == '__main__':
    N = int(input())

    for i in range(N):
        command = input()

        com, value, index = get_command(command)

        if dic.get(com):
            dic[com](value, index)
