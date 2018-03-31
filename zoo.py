import random

class Bird:
    name=""
    sound=""

    def __init__(self,n,s):
        self.name = n
        self.sound = s
    def makeSound(self):
        print(self.name," is making sound ",self.sound," in the Zoo.")


class Animal:
    name = ""
    sound = ""

    def __init__(self, n, s):
        self.name = n
        self.sound = s

    def makeSound(self):
        print(self.name, " is making sound ", self.sound, " in the Zoo.")


zoo=[]
size=0
c="Yes"
print("Zoo is Open Now!!!")

while(c=="Yes" or c=="yes"):
    print("What do you want to enter in the zoo ?? Animal Or A Bird ??")
    choice=input()
    if(choice=="animal" or choice=="Animal"):
        print("Which animal do you want to enter ???")
        name=input()
        print("What Sound Does It make??")
        sound=input()
        animal=Animal(name,sound)
        zoo.append(animal)
        size+=1
    if(choice == "bird" or choice=="Bird"):
        print("Which bird you want to enter in the zoo???")
        name=input()
        print("What sound does it make???")
        sound=input()
        bird=Bird(name,sound)
        zoo.append(bird)
        size+=1
    print("Do you want to Enter aany other animal or bird in the zoo???")
    print("Enter Yes for more Or No to simply exit!!!!")
    c=input()

for i in range (0,size):
    r=random.choice(zoo)
    r= makeSound ()
    #zoo[i].makeSound()
print("<<<<<<<Zoo is closed now>>>>>>>")