"""Проверьте, является ли данный массив возрастающим или убывающим."""

"""if   len(n)!=1 and n[0]>n[1] :
    print("Убывающий")
elif len(n)!=1 and n[0]<n[1] :
    print("Возрастающий")
else:
    print("НЕ убывающий НЕ возрастающий")"""


n=list(map(int,input().split()))
q=0
a=n[0]
for i in range (len(n)):
    if i==0  :
        pass
    elif n[i]<a:
       q=q-1
    elif n[i]>a :
        q=q+1
    a=n[i]
else:
    if q>0:
        print("Возрастающий" )
    elif q<0:
        print("Убывающий")
    else:    
     print("НЕ убывающий НЕ возрастающий")
