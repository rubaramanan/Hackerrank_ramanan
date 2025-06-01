# Enter your code here. Read input from STDIN. Print output to STDOUT

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math


def get_mbc(ab: int, bc: int):
    if ab == bc:
        return 45
    x = ab / bc
    tan_inv = math.atan(x)
    return round(math.degrees(tan_inv))


ab = int(input())
bc = int(input())

print(f'{get_mbc(ab, bc)}\N{DEGREE SIGN}')
