list1, list2 = [], []
max1 = 0
m = int (input ("Enter row size: "))
n = int (input ("Enter column size: "))
print ("Enter Elements: ")
for i in range (0, m):
    for i in range (0, n):
        temp = int (input ( ))
        if max1 < temp:
            max1 = temp
        list1.append (temp)
    list2.append (list1)
    list1 = []
print (list2)
print ("Max Element:", max1)