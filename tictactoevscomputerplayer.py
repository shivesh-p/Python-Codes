# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 14:29:52 2018

@author: @shivesh_pandey
"""
import random    
board=[['_' for i in range (3)] for j in range (3)]
for i in range (0,3):
    for j in range(0,3):
        print(board[i][j],end=" ")
    print("\n")
class check:
    
    def checkHorizontal(self):
        
        for j in range (0,3):
            ch1=1
            for i in range(0,3):
                if(board[j][i]=='X'):
                    ch1+=1
            if(ch1==4):
                return 1
        
        for j in range (0,3):
            ch2=1
            for i in range(0,3):
                if(board[j][i]=='O'):
                    ch2+=1
            if(ch2==4):
                return 0
            
    def checkVertical(self):
        
        for j in range (0,3):
            cv1=1
            for i in range(0,3):
                if(board[i][j]=='X'):
                    cv1+=1
            if(cv1==4):
                return 1
        
        for j in range (0,3):
            cv2=1
            for i in range(0,3):
                if(board[i][j]=='O'):
                    cv2+=1
            if(cv2==4):
                return 0
            
    def checkSlash(self):
        
        if((board[0][0]=='X' and board[1][1]=='X' and board[2][2]=='X') or(board[0][2]=='X' and board[1][1]=='X' and board[2][1]=='X')):
            return 1
        elif((board[0][0]=='O' and board[1][1]=='O' and board[2][2]=='O') or(board[0][2]=='O' and board[1][1]=='O' and board[2][1]=='O')):
            return 0



choice=1
count=0
while(choice==1):
    print("Player 1 You have your move as X")
    rc=random.randrange(1,4,1)
    cc=random.randrange(1,4,1)
    if(count%2==0):
        print("Enter Row No:")
        r=int(input())
        print("Enter Column No:")
        c=int(input())
        board[r-1][c-1]='X'
        count+=1
    else:
        q=1
        rc=random.randrange(1,4,1)
        cc=random.randrange(1,4,1)
        while(q==1):
            if(board[rc-1][cc-1]=='_'):
                board[rc-1][cc-1]='O'
                q=0
            else:
                rc=random.randrange(1,4,1)
                cc=random.randrange(1,4,1)
                q=1
        count+=1
    for i in range (0,3):
        for j in range(0,3):
            print(board[i][j],end=" ")
        print("\n")
    c=check()
    if(count>5):
        if(c.checkHorizontal()==1 or c.checkVertical()==1 or c.checkSlash()==1):
            print("Player ! You Win!!!")
            choice=0
        if(c.checkHorizontal()==0 or c.checkSlash()==0 or c.checkVertical()==0):
            print("Computer Wins!!!   You Lose !!!!")
            choice=0




















