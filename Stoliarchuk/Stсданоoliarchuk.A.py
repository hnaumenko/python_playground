n=int(input("Введите количество удавов: "))
a=""
for i in range(n):
	s=input()
	if len(s)<=10:
		a=s+a
print(a)