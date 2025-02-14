n = int(input())
s = set(map(int, input().split()))
num = int(input())

operations = [input().split() for i in range(num)]


def do_operation(operation):
    op = operation[0]
    try:
        if op == 'pop':
            return s.pop()

        if op == 'remove':
            param = operation[1]
            return s.remove(int(param))
    except Exception as E:
        return E
    if op == 'discard':
        param = operation[1]
        return s.discard(int(param))


for operation in operations:
    do_operation(operation)

print(sum(list(s)))