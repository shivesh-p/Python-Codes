board=[['_' for i in range (3)]for j in range (3)]
for i in range (0,3):
    for j in range(0,3):
        print(board[i][j],end="  ",sep="  ")
    print("\n")
print("Player 1 ! You have X as your move.")
class check:

    def checkHorizontal(self):

        for j in range(0,3):
            ch1=1
            for i in range (0,3):
                if(board[j][i]=='X'):
                    ch1+=1
            if(ch1==4):
                print("H1")
                return 1
        for j in range(0,3):
            ch2=1
            for i in range (0,3):
                if(board[j][i]=='O'):
                    ch2+=1
            if (ch2 == 4):
                print("H2")
                return 0
    def checkVertical(self):

        for j in range(0, 3):
            cv1 = 1
            for i in range(0, 3):
                if (board[i][j] == 'X'):
                    cv1 += 1
            if (cv1 == 4):
                print("V1")
                return 1
        for j in range(0, 3):
            cv2 = 1
            for i in range(0, 3):
                if (board[i][j] == 'O'):
                    cv2 += 1
            if (cv2 == 4):
                print("V2")
                return 0
    def checkSlash(self):
        if((board[0][0]=='X' and board[1][1]=='X' and board[2][2]=='X') or (board[0][2]=='X' and board[1][1]=='X' and board[2][0]=='X')):
            return 1
        if((board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O') or (board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O')):
            return 0
count=0
for i in range(0,9):
    print("Players Enter your chances or positions on the board one by one Starting from Player 1.")
    a=int(input("Enter the Row no: "))
    b=int(input("Enter the Column Number: "))
    if(i%2==0):
        board[a-1][b-1]='X'
    else:
        board[a-1][b-1]='O'
    count+=1
    for i in range(0,3):
        for j in range(0,3):
            print(board[i][j],end=" ",sep=" ")
        print("\n")
    if(count>=5):
        c=check()
        if(c.checkHorizontal()==1 or c.checkSlash()==1 or c.checkVertical()==1):
            print("Player 1 Wins !!!!!")
            break
        if (c.checkHorizontal() == 0 or c.checkSlash() == 0 or c.checkVertical() == 0):
            print("Player 2 Wins !!!!!")
            break
