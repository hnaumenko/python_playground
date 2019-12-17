"""Найти количество чисел в массиве, которые делятся на 3, но не делятся на 7."""
n=list(map(int,input().split()))
c=0
for i in n:    
    if i%3==0 and i%7!=0:
        c=c+1
print(c)
    
