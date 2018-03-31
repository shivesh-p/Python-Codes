"""16. Read a number. Do half of number after last odd digit. multiply by 3 the number obtained. Input 61389426
output 184167639 (61389213*3). Input 87 output 261. Input 78 output 222 (74*3)."""
y=0
z=0
count=0
x=int(input("Enter the number:"))
while(x>0):
	y=x%10
	if(y%2 is not 0):
		break;
	x = x/10
	z=(int)(z+y*(10**count))
	count+=1;
z=z/2;
x=(int)(x*(10**count))
x=(x+z)*3;
print(x)
