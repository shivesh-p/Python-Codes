from random import randint
 
t = ["Rock", "Paper", "Scissors"]
computer = t[randint(0,2)]
player = False
cc=0
cp=0
while( player == False and cc<3 and cp<3):
    player = input("Rock, Paper, Scissors?")
    if( player == computer):
        print("Tie!")
    elif( player == "Rock"):
        if (computer == "Paper"):
            cc+=1          
            print("You lose!")
        else:
            print("You win!")
            cp+=1
    elif (player == "Paper"):
        if computer == "Scissors":
            print("You lose!")
            cc+=1
        else:
            print("You win!")
            cp+=1
    elif (player == "Scissors"):
        if computer == "Rock":
            print("You lose...")
            cc+=1
        else:
            print("You win!")
            cp+=1
    else:
        print("Invalid Input.Check your spelling!")
    player = False
    computer = t[randint(0,2)]
