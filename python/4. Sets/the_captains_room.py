# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
rooms = list(map(int, input().split()))
room_no = set(rooms)


s = sum(room_no)*k
a = sum(rooms)
c = (s - a) // (k-1)
print(c)