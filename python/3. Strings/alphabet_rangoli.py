def gen_rangoli_line(size: int, index: int):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f',
                'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    chars = [alphabet[size - 1 - i] for i in range(index + 1)]
    line = '-'.join(chars + chars[:-1][::-1])
    return line.center((4 * size - 3), '-')


def print_rangoli(size):
    if size == 1:
        print('a')
        return
        # your code goes here
    lines = [gen_rangoli_line(size, i) for i in range(size)]
    print('\n'.join(lines + lines[-2::-1]))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
