
n=1
m=0
x=int(input("Enter the Value of the number:"))
while(x>0):
    m=x%10
    m=m*n
    print(m)
    n=n*10
    x=x/10
