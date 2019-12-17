"""Заменить каждый элемент массива с четным номером на соседний слева элемент."""
n=list(input().split())
for i in range (len(n)):
    if  i!=0 and i%2==0:
        n[i]=n[i-1]
    elif i==0:
        n[0]=n[len(n)-1]
print(*n)    
        
