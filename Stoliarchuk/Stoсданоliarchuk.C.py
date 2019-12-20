p=input("Состав вещества: ")
L=len(p)
k=1
c=p[0]
d=p[1]
if d.isupper():
	for q in range(1,L):
		a=p[q]
		if c!=a and a.isupper():
			k+=1
	for i in range(1,L-1):
		r=p[i]
		s=p[i+1]
		if s.isupper():
			for e in range(2,L):
				t=p[e]
				if e<L-1:
					y=p[e+1]
					if r==t and t.isupper() and r!=c and y.isupper() and r!=p[i] and i in range(i):
						k-=1
					else :
						t=t+y
						if r==t and t.isupper() and r!=c:
							k-=1
				else :
					if r==t and t.isupper() and r!=c and y.isupper() :
						k-=1
					
		else:
			r=r+s
			for e in range(3,L):
				t=p[e]
				if r==t and r.isupper() and t.isupper():
					k-=1
else:
	c=c+d
	for q in range(2,L):
		a=p[q]
		if c!=a and a.isupper():
			k+=1
	for i in range(2,L-1):
		r=p[i]
		s=p[i+1]
		if s.isupper():
			for e in range(3,L):
				t=p[e]
				if e<L-1:
					y=p[e+1]
					if r==t and t.isupper() and y.isupper() :
						k-=1
					else :
						t=t+y
						if r==t and t.isupper() and r!=c:
							k-=1
				else :
					if r==t and t.isupper() and r!=c and y.isupper() :
						k-=1
					
		else:
			r=r+s
			for e in range(3,L):
				t=p[e]
				if r==t and r.isupper() and t.isupper():
					k-=1
print(k)

	