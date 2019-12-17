"""Дан массив. Найдите два соседних элемента, сумма которых минимальна."""
n=list(map(int,input().split()))
a=n[0]
b=n[1]
for i in range (len(n)):
    if i!=0 and  i!=1 and a+b>n[i]+n[i-1]:
        a=n[i-1]
        b=n[i]
print(a,b)    
        
