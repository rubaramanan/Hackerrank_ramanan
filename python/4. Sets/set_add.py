# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
country = set()
for i in range(n):
    country.add(input())

l = list(country)
print(len(l))
