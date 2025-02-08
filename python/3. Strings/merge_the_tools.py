def get_unique_chars(string):
    l = list(sorted(set(string), key=string.index))
    return ''.join(l)


def merge_the_tools(string, k):
    # your code goes here
    t = []
    for i in range(0, len(string), k):
        t.append(string[i:i + k])

    for i in t:
        u = get_unique_chars(i)
        print(u)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
