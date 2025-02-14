n_eng = input()
eng_ind = set(map(int, input().split()))
n_french = input()
fre_ind = set(map(int, input().split()))

# s.intersection(str/list/set)
s = fre_ind & eng_ind
print(len(s))
