"""Найдите наименьший четный элемент массива."""
n=list(map(int,input().split()))
m=[]
for i in n:
    if  i%2==0:
        m=m+[i]
print(min(m))        
