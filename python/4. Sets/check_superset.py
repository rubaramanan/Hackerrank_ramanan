# Enter your code here. Read input from STDIN. Print output to STDOUT

def check_sperset(a, b):
    return (a <= b) and (a != b)


b = set(map(int, input().split()))
n = int(input())
l = []
for i in range(n):
    a = set(map(int, input().split()))
    l.append(check_sperset(a, b))

print(all(l))
