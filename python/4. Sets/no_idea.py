# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = tuple(map(int, input().split()))
l = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))
# print(l,a,b)

x = []

a_c = sum(1 for x in l if x in a)
b_c = sum(1 for x in l if x in b)
print(a_c - b_c)