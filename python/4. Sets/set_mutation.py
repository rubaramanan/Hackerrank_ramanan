# #.update() or |=
# h = set('Hacker')
# r = set('Rank')
# h.update(r)
# print(h)
#
# #.intersection_update() or &=
# h = set('Hacker')
# r = set('Rank')
#
# h.intersection_update(r)
# print(h)
#
# # .difference_update() or -=
# h = set('Hacker')
# r = set('Rank')
#
# h.difference_update(r)
# print(h)
#
# # .symmetric_difference_update() or ^=
# h = set('Hacker')
# r = set('Rank')
#
# h.symmetric_difference_update(r)
# print(h)


# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
num = set(map(int, input().split()))
x = int(input())
operations = [input().split() for i in range(x * 2)]


def do_operation(operation: list):
    op = operation[0][0]
    param_set = set(map(int, operation[1]))

    if op == 'intersection_update':
        return num.intersection_update(param_set)
    if op == 'update':
        return num.update(param_set)
    if op == 'symmetric_difference_update':
        return num.symmetric_difference_update(param_set)
    if op == 'difference_update':
        return num.difference_update(param_set)


for i in range(0, x * 2, 2):
    do_operation(operations[i:i + 2])

print(sum(num))