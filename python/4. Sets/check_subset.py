def check_subset(a, b):
    # method 1
    # return a.issubset(b)

    #method2
    # return a<=b

    #method3
    return all(i in b for i in a)

t = int(input())
for i in range(t):
    a_l = int(input())
    a = set(map(int, input().split()))
    b_l = int(input())
    b = set(map(int, input().split()))
    
    print(check_subset(a,b))