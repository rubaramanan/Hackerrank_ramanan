# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
m_v = set(map(int, input().split()))
n = int(input())
n_v = set(map(int, input().split()))

s = sorted(m_v ^ n_v)
for i in s:
    print(i)
