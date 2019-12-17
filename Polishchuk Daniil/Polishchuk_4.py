"""Найдите сумму нечетных чисел списка, которые не превосходят 11."""
n=list(map(int,input().split()))
c=0
for i in n:
    if i<11 and i%2!=0:
        c=c+1
print(c)
    

