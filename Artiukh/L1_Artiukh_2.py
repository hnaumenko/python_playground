'''
«2»: Ввести два натуральных числа a и b и заполнить массив
из 10 элементов случайными числами в диапазоне между
a и b (a может быть больше b).
'''
from random import randint
a,b=map(int,input('Введите диапазон: ').split())
if a<b:
	c=[ randint(a,b) for i in range(10) ]
else:
	c=[ randint(b,a) for i in range(10) ]
print(*c)