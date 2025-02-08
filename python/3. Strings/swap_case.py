def do_swap(c):
    if c.islower():
        return c.upper()
    if c.isupper():
        return c.lower()
    if not c.isalpha():
        return c


def swap_case(s):
    swap_c = [do_swap(c) for c in list(s)]

    return ''.join(swap_c)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
