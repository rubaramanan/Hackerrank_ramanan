# Enter your code here. Read input from STDIN. Print output to STDOUT

import cmath


def polar_conv(num: complex):
    q = cmath.phase(num)
    r = abs(num)

    return r, q


num = complex(input())
r, q = polar_conv(num)

print(r)
print(q)
