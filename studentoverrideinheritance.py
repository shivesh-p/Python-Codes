
class student:

    name=""

    year=18

    def __init__(self,name,year):

        self.name = name
        self.year = year

    def display(self):

        print("The name of the student is : ",self.name)
        print("The year of the student is: ",self.year)

class faculty(student):

    fname=""

    fsubject=""

    def __init__(self,name,year,fname,fsubject):

        student.__init__(self,name,year)
        self.fname = fname
        self.fsubject = fsubject

    def display(self):

        print ("The name of the faculty is :", self.fname)
        print ("The subject faculty teaches is :", self.fsubject)

class branch(faculty):

    bname=""

    bcode=""

    def __init__(self,name,year,fname,fsubject,bname,bcode):

        faculty.__init__(self,name,year,fname,fsubject)
        self.bname = bname
        self.bcode = bcode

    def display(self):

        print ("The name of the branch in which the student studies is :", self.bname)
        print ("The branch code of the branch in which the student studies is :", self.bcode)

class department(branch):

    dname=""

    def __init__(self,name,year,fname,fsubject,bname,bcode,dname):

        branch.__init__(self,name,year,fname,fsubject,bname,bcode)
        self.dname = dname

    def display(self):

        print("The name of the department which contains both the faculty and the student is: ", self.dname)


class university (department):

    uname = ""

    dno = 0

    x=5

    def __init__(self, name, year, fname, fsubject, bname, bcode, dname,uname,dno):

        department.__init__ (self, name, year, fname, fsubject, bname, bcode,dname)
        self.uname = uname
        self.dno = dno

    def display(self):

        print ("The name of the university which the student studies is: ", self.uname)
        print ("The number of the departments in the university is: ", self.dno)

    def display(self, x):

        print ("The name of the university which the student studies is: ", self.uname)
        print ("The number of the departments in the university is: ", self.dno)
        print("The no of years of university", self.x)

u=university("Shivesh Pandey",1,"Anuj Mahajan","Programming in Python","Computer Science","CSL 1023","Department Of Engineering","Shri Mata Vaishno Devi University, Kakryal , Katra 182320",8)
u.display(5)
