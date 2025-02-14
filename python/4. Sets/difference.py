# Enter your code here. Read input from STDIN. Print output to STDOUT
n_eng = input()
eng_ind = set(map(int, input().split()))
n_french = input()
fre_ind = set(map(int, input().split()))

# eng_ind.difference(fre_ind)
s = eng_ind - fre_ind
print(len(s))
