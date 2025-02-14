# Enter your code here. Read input from STDIN. Print output to STDOUT
n_eng = int(input())
eng_ind = set(map(int, input().split()))
n_french = int(input())
french_ind = set(map(int, input().split()))

# s.union(str/list/set)
se = french_ind | eng_ind
print(len(list(se)))