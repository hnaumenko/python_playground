"""Даны две дроби a/b и c/d(числа a и c — целые, b и d — натуральные).
Вычислите их
сумму и запишите ее в виде смешанной дроби x y/z(число xцелое, числа y z целое
натуральные, дробь y/z— правильная несократимая)."""
a,b,c,d=map(int,input().split())
if b>d:
    q=b//d
    a=a*q
elif d>b:
    q=d//b
    c=c*q
else:
    s=(a+c)/b
print(q)

