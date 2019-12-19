from random import *
s=input()
if s=="test":
    h=input()
    h=str(h)
    k=0
    n=1
    kys=0
    kym=0
    while k<1:
        s=input()
        if s==h:
            print("Вы угадали")
            print("Количество попыток:",n)
            k+=1
        else :
            for i in str(h):
                if i==s[0] or i==s[1] or i==s[2] or i==s[3]:
                    kys+=1
            print("Вы угадали цифр:",kys)
            kys=0
            for i in range (4):
                if h[i]==s[i]:
                    kym+=1
            print("Вы угадали цифр и позиций:",kym)
            kym=0
        n+=1
elif s=="+":
    h=randint(1000,9999)
    h=str(h)
    q=0
    p=0
    while p==0:
        for i in range (4):
            if h[i]==h[0] or h[i]==h[1] or h[i]==h[2] or h[i]==h[3] :
                q+=1
            if q>1:
                h=randint(1000,9999)
                h=str(h)
            else: p+=1
    k=0
    n=1
    kys=0
    kym=0
    while k<1:
        s=input()
        if s=="End":
            print(h)
            k+=1
            break
        if s==h:
            print("Вы угадали")
            print("Количество попыток:",n)
            k+=1
        else :
            for i in str(h):
                if i==s[0] or i==s[1] or i==s[2] or i==s[3]:
                    kys+=1
            print("Вы угадали цифр:",kys)
            kys=0
            for i in range (4):
                if h[i]==s[i]:
                    kym+=1
            print("Вы угадали цифр и позиций:",kym)
            kym=0
        n+=1