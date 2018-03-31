m=int(input('Enter the no of rows'))
n=int(input('Enter the no of columns'))
arr2d1=[]
result=[]
arr2d2=[]
print('Enter the First matrix')
for i in range(0,m):
    arr1d=[]
    for j in range(0,n):
        print('Enter the element at index',i,j)
        x=int(input())
        arr1d.append(x)
    arr2d1.append(arr1d)
print('Enter the second matrix')
for i in range(0,m):
    arr1d=[]
    for j in range(0,n):
        print('Enter the element at index',i,j)
        x=int(input())
        arr1d.append(x)
    arr2d2.append(arr1d)
for i in range(0,m):
    for j in range(0,n):
        result[i][j] =arr2d1[i][j] + arr2d1[i][j]

for r in result:
   print(r)
