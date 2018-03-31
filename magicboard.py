class mboard():
  board=[[0 for i in range (3)] for j in range (3)]
  def rowset(self,x):
    for i in range (3):
      self.board[x][i]=1
      
  def colset(self,x):
    for i in range (3):
      self.board[i][x]=1
      
  def rowquery(self,x):
    rq=0
    for i in range (3):
      if(self.board[x][i]==1):
        rq+=1
    print("Row Query",rq)
    
  def colquery(self,x):
    cq=0
    for i in range (3):
      if(self.board[i][x]==1):
        cq+=1
    print("Column query",cq)
    
  def show(self):
    for i in range (3):
      for j in range (3):
        print(self.board[i][j],end="")
      print()
      
bo=mboard()
print("How many operations do you want to perform??")
n=int(input())
for i in range (n):
  print("1 for Row Set")
  print("2 for Column Set")
  print("3 for Row Query")
  print("4 for Column Query")

  p=int(input())
  if(p==1):
    print("Enter Row No")
    q=int(input())
    bo.rowset(q)
  elif(p==2):
    print("Enter Column No")
    r=int(input())
    bo.colset(r)
  elif(p==3):
    print("Enter Row No")
    s=int(input())
    bo.rowquery(s)
  elif(p==4):
    print("Enter Column No")
    t=int(input())
    bo.colquery(t)
bo.show()
