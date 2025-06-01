def split_and_join(line):
    # write your code here
    strs = line.split(" ")
    return '-'.join(strs)


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
