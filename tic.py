board=[['_' for i in range (3)]for j in range (3)]
for i in range (0,3):
    for j in range(0,3):
        print(board[i][j],end=" ",sep="|")
    print("\n")
print("Player 1 ! What do You Chose X or O ??")
p1=input()
class check:
    def checkHorizontal(self):
        x=0
        for i in range (0,3):
            if(board[x][i]=='X'):
                return 1;
                break
            if(board[x][i]=='O'):
                return 0;
                break
            x+=1;
    def checkVertical(self):
        x=0
        for i in range (0,3):
            if(board[i][x]=='X'):
                return 1;
                break
            if(board[i][x]=='O'):
                return 0;
                break
            x+=1;
    def checkSlash(self):
            if(board[0][0]=='X' or board[1][1]=='X' or board[2][2]=='X'):
                return 1;
            else:
                return 0;
            x+=1;
count=0
if(p1=='X'):
    for i in range(0, 9):
        print("Players Enter your chances or positions on the board one by one Starting from Player 1.")
        a = int(input("Enter the Row no: "))
        b = int(input("Enter the Column Number: "))
        if (i % 2 == 0):
            board[a - 1][b - 1] = 'X'
        else:
            board[a - 1][b - 1] = 'O'
        count += 1
        for i in range(0, 3):
            for j in range(0, 3):
                print(board[i][j], end=" ", sep="|")
            print("\n")
        if (count >= 5):
            c = check();
            c.checkHorizontal()
            c.checkVertical()
            c.checkSlash()
            if (c.checkHorizontal() == 1 or c.checkSlash() == 1 or c.checkVertical() == 1):
                print("Player 1 Wins !!!!!")
                break
            if (c.checkHorizontal() == 0 or c.checkSlash() == 0 or c.checkVertical() == 0):
                print("Player 2 Wins !!!!!")
                break
else:
    for i in range(0, 9):
        print("Players Enter your chances or positions on the board one by one Starting from Player 1.")
        a = int(input("Enter the Row no: "))
        b = int(input("Enter the Column Number: "))
        if (i % 2 == 0):
            board[a - 1][b - 1] = 'O'
        else:
            board[a - 1][b - 1] = 'X'
        count += 1
        for i in range(0, 3):
            for j in range(0, 3):
                print(board[i][j], end=" ", sep="|")
            print("\n")
        if (count >= 5):
            c = check();
            c.checkHorizontal()
            c.checkVertical()
            c.checkSlash()
            if (c.checkHorizontal() == 1 or c.checkSlash() == 1 or c.checkVertical() == 1):
                print("Player 2 Wins !!!!!")
                break
            if (c.checkHorizontal() == 0 or c.checkSlash() == 0 or c.checkVertical() == 0):
                print("Player 1 Wins !!!!!")
                break