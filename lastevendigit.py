
j=0
l=1
m=0;
n=int(input('Enter the Value of the number:'))
while(n>0):
    i=n%10;
    if(i%2==0):
        k=i
        break
    n=n/10;
print('Last of even digits:',k);
