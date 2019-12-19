s=input("Введите битовую строку: ")
l=len(s)
k=0
for i in range(l):
	if s[i]=="1":
		k+=1
if k%2==0:
	s=s+"0"
else: s=s+"1"
print(s)