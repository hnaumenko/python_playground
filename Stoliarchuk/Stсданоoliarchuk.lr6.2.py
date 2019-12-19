s=input()
s=s.lower()
s=s.replace(' ','')
s=s.replace(':','')
s=s.replace("'",'')
s=s.replace('-','')
s=s.replace('\v','')
s=s.replace(',','')
s=s.replace('!','')
s=s.replace('.','')
l=len(s)
k=1
for i in range(l):
	if s[i]!= s[-1-i]:
		k=0
if k==1: 
	print("Является")
else: print("Не является")