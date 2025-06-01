# Enter your code here. Read input from STDIN. Print output to STDOUT

inp = input()

l = inp.split()

n = int(l[0])
m = int(l[1])
c = '.|.'
for i in range(n):
    if i < n // 2:
        print((c + c * (i * 2)).center(m, '-'))
    if i == n // 2:
        print('WELCOME'.center(m, '-'))
    if i > n // 2:
        x = n - (i - n // 2) * 2
        print((c * (x)).center(m, '-'))
