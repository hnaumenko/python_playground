print()
a,b=map(float,input().split())
d,c=map(float,input().split())
z=input()
k=0
if z==">":
	k+=1
if a!=1 :
	b=b/a
	a=1
if d!=1:
	c=c/d
	d=1
b1=-b
c1=-c
if b1>c1:
	o1=((-b1+1)+b)*((-b1+1)+c)
	if k==1:
		if o1>0:
			print("x",">",b1,"and","x","<",c1)
		else: print(c1,"<","x","<",b1)
	elif k==0:
		if o1>0:
			print(c1,"<","x","<",b1)
		else:
			print("x",">",b1,"and","x","<",c1)
else:
	o1=((-c1+1)+b)*((-c1+1)+c)
	if k==1:
		if o1>0:
			print("x",">",c1,"and","x","<",b1)
		else: print(b1,"<","x","<",c1)
	elif k==0:
		if o1>0:
			print(b1,"<","x","<",c1)
		else:
			print("x",">",b1,"and","x","<",c1)











