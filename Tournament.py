class player:
    name=""
    age=0
    gender=""
    def inputPlayerDetails(self):
        self.name=input("Enter the name of the player:")
        self.age=int(input("Enter the age of the player:"))
        self.gender=input("Enter your sex:")
    def displayPlayerDetails(self):
        print("Name: ",self.name,"Age: ",self.age,"Sex: ",self.gender)
        print("\n")
class Team:
    nameofTeam=[]
    sizeOfTeam=1
    noOfTeams=1
    arrayOfPlayers=[]
    def inputTeamDetails(self):
        self.noOfTeams=int(input("Enter the Number of Teams: "))
        self.sizeOfTeam=int(input("Enter the Size Of the Team: "))
        print("Enter the details of ",self.noOfTeams," Teams")
        for i in range(0,self.noOfTeams):
            n = input("Enter the name of the Team: ")
            self.nameofTeam.append(n)
            for j in range(0,self.sizeOfTeam):
                p=player()
                p.inputPlayerDetails()
                self.arrayOfPlayers.append(p)
    def displayTeamDetails(self):
        for j in range(0,self.noOfTeams):
            print("The details of team ",self.nameofTeam[j],"are: ")
            for i in range(0,self.sizeOfTeam):
                print("Details Of Player ",i+1,": ")
                self.arrayOfPlayers[i].displayPlayerDetails()
"""
t=Team()
t.inputTeamDetails()
t.displayTeamDetails()
"""
class Tournament:
    nameOfTournaments="s"
    arrayOfTeams=[]
    noOfTeam=1
    def inputTournamentDetails(self):
        self.noOfTeams=int(input("Enter the number of teams: "))
        self.nameOfTournaments=input("Enter the name of the tournament: ")
        y=Team()
        y.inputTeamDetails()
        self.arrayOfTeams.append(y)
    def displayTournamentDetails(self):
        print("The details of Tournament ",self.nameOfTournaments,"are:")
        for i in range(0,self.noOfTeam):
            self.arrayOfTeams[i].displayTeamDetails()
"""
k=Tournament()
k.inputTournamentDetails()
k.displayTournamentDetails()
"""
class Olympics:
    noOfTournaments=1
    arrayOfTournaments=[]
    def inputOlympicsDetails(self):
        self.noOfTournaments=int(input("Enter the Number of the Tournaments: "))
        print("Enter the details of ",self.noOfTournaments," Tournaments")
        for i in range(0,self.noOfTournaments):
            print("Enter the details of Tournament Number: ",i+1)
            d=Tournament()
            d.inputTournamentDetails()
            self.arrayOfTournaments.append(d)
    def displayOlympicsDetails(self):
        for i in range(0,self.noOfTournaments):
            print("The details of Tournament Number ",(i+1),"are:")
            self.arrayOfTournaments[i].displayTournamentDetails()
q=Olympics()
q.inputOlympicsDetails()
q.displayOlympicsDetails()