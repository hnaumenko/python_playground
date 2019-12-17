'''
«3»: Ввести два натуральных числа a и b и заполнить массив
из 10 элементов: первая половина массива заполняется
случайными числами в диапазоне между a и b (a может
быть больше b), а вторая половина массива содержит их
квадраты в том же порядке.
'''
from random import randint
a,b=map(int,input('Введите диапазон: ').split())
if a<b:
	c=[randint(a,b) for x in range(5)]
else:
	c=[randint(b,a) for x in range(5)]
for i in range(5):
    c=c+[c[i]**2]
print(*c)

