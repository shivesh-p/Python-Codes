class person:
    """
    def inputDetails(self):
        self.fname=input("Enter the name of the employee: ")
        self.sname=input("Enter the surname of the employee: ")
    """
    def __init__(self,fname,sname):
        self.fname = fname
        self.sname = sname
    def displayDetails(self):
        print("The name of the employee is: ",self.fname," ",self.sname)

"""
p=person("Kumar","Aditya")
p.displayDetails()"""

class employee(person):
    def __init__(self,fname,sname,eid,salary):
        person.__init__(self,fname,sname)
        """
        self.fname = fname
        self.sname = sname
        """
        self.eid = eid
        self.salary = salary
    def displayEmployee(self):
        print ("The name of the employee is: ", self.fname, " ", self.sname)
        print ("The employee id of the employee is: ", self.eid)
        print ("The salary of the employee is: ", self.salary)
class manager(employee):
    def __init__(self,fname,sname,eid,salary,bonus):
        employee.__init__(self,fname,sname,eid,salary)
        """
        self.eid = eid
        self.salary = salary
        self.fname = fname
        self.sname = sname
        """
        self.bonus = bonus

    def displayManager(self):
        print ("The name of the employee is: ", self.fname, " ", self.sname)
        print ("The employee id of the employee is: ", self.eid)
        print ("The salary of the employee is: ", self.salary)
        print ("The bonus of the employee is: ",self.bonus)

class tata:
    bookid=12
    currentvalue=90
    def displaytata(self):
        print ("The book value of the share was : ", self.bookid)
        print ("The current value of the share is : ", self.currentvalue)


class executive(manager,tata):
    def __init__(self,fname,sname,eid,salary,bonus,shares,bookid,currentvalue):
        manager.__init__ (self, fname, sname, eid, salary ,bonus)
        tata.bookid = bookid
        tata.currentvalue = currentvalue
        """
        self.eid = eid
        self.salary = salary
        self.fname = fname
        self.sname = sname
        self.bonus = bonus
        """
        self.shares = shares

    def displayExecutive(self):
        print ("The name of the employee is: ", self.fname, " ", self.sname)
        print ("The employee id of the employee is: ", self.eid)
        print ("The salary of the employee is: ", self.salary)
        print ("The bonus of the employee is: ", self.bonus)
        print ("The bonus of the employee is: ", self.shares)
        print ("The book value of the share is: ", self.bookid)
        print ("The current value of the share is: ", self.currentvalue)

"""
e=executive("Kumar","Aditya", 16789212,180000,12000,50)
e.displayExecutive()
"""

e=executive("kUMAR","aDITYA",16216654,1820000,13000,85,9087,9055)
e.displayExecutive()