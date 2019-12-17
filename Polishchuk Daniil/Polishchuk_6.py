"""Проверьте, образует ли элементы массива в данном порядке арифметическую или
геометрическую прогрессии."""
n=list(map(int,input().split()))
a=n[0]
b=n[1]
d=0
if len(n)==2:
        print("арифметическая")
else:        
    for i in  range (len(n)):
        if i==0 or i==1:
            pass
        else:
            if abs(b-a)==abs(n[i]-b):
                d=d+1
            elif abs(b/a)==abs(n[i]/b):
                d=d-1
            else:
                print("НЕ являеться арифметической и геометрической прогрессией")
                break
        a=b
        b=n[i]
    else:
        if d>0:
            print("Являеться Ариметической прогрессией")
        else:
            print("Являеться Геометрической прогрессией")
