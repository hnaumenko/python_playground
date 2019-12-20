a=int(input())
b=int(input())
c=int(input())
d=int(input())
s=''
for i in range (c,d+1):
    s+='\t%s'%i
for i in range(a,b+1):
    s+='\n%s'%i
    for n in range (c,d+1):
        s+='\t%s'%(i*n)
print(s)