s=input("Введите битовую строку: ")
l=len(s)
s1=""
for i in range(l):
	if s[i]=="1":
		s1=s1+"0"
	else: s1=s1+"1"
print("Инверсия: ",s1)
