print("Введите координаты короля: ")
x1,y1=map(int,input().split())
print("Введите координаты коня: ")
x2,y2=map(int,input().split())
if  x1==x2 and y1==y2 :
	print("Невозможные координаты")
elif  x1<=8 and y1<=8 and x2<=8 and y2<=8 :
	dx=abs(x2-x1) 
	dy=abs(y2-y1) 
	if dx==1 and dy==2 or dx==2 and dy==1: 
		o1="Y"
	else : o1="N"
	if dx==2 and dy==4 or dx==4 and dy==2 or dx==4 or dy==4 or dx==1 and dy==1:
		o2="Y"
	else : o2="N"
	if abs(x1-x2)<=1 and abs(y1-y2)<=1:
		o3="Y"
		o4="N"
	elif abs(x1-x2)<=2 and abs(y1-y2)<=2 :
		o3="N"
		o4="Y"
	print(o1,o2,o3,o4,sep="")
else: print("Невозможные координаты")
