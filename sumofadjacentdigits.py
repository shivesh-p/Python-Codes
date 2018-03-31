"""17. Write program, which finds the sum of numbers formed by consecutive digits. Input 2415
output 24+41+15=80"""
y=0
z=0
sum=0
m=0
x=int(input("Enter the Number:"))
while (x>9):
   	y=x%10;
   	x=x/10;
   	z=x%10;
   	m=z*10;
	sum=sum+y+m;
print("sum of numbers formed by consecutive digits= ",sum)
