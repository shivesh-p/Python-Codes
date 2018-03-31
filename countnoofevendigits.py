j=0
l=1
n=int(input('Enter the Value of the number:'))
while(n>0):
    i=n%10;
    if(i%2==0):
    	j+=1;
    n=n/10
print('Number of even digits:',j);
