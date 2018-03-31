
class student:

    name=""

    year=2

    def __init__(self,name,year):

        self.name = name
        self.year = year

    def displayStudent(self):

        print("The name of the student is : ",self.name)
        print("The year of the student is: ",self.year)

class faculty(student):

    fname=""

    fsubject=""

    def __init__(self,name,year,fname,fsubject):

        student.__init__(self,name,year)
        self.fname = fname
        self.fsubject = fsubject

    def displayFaculty(self):

        print("The name of the student is :",self.name)
        print ("The year of study of the student is :", self.year)
        print ("The name of the faculty is :", self.fname)
        print ("The subject faculty teaches is :", self.fsubject)

class branch(faculty):

    bname=""

    bcode=""

    def __init__(self,name,year,fname,fsubject,bname,bcode):

        faculty.__init__(self,name,year,fname,fsubject)
        self.bname = bname
        self.bcode = bcode

    def displayBranch(self):

        print("The name of the student is: ",self.name)
        print ("The year of the student is: ", self.year)
        print ("The branch of the student is: ", self.fname)
        print ("The branch code of the student is: ", self.fsubject)
        print ("The name of the branch in which the student studies is :", self.bname)
        print ("The branch code of the branchb in which the student studies is :", self.bcode)

class department(branch):

    dname=""

    def __init__(self,name,year,fname,fsubject,bname,bcode,dname):

        branch.__init__(self,name,year,fname,fsubject,bname,bcode)
        self.dname = dname

    def displayDepartment(self):

        print("The name of the student is: ",self.name)
        print ("The year of the student is: ", self.year)
        print ("The branch of the student is: ", self.fname)
        print ("The branch code of the student is: ", self.fsubject)
        print ("The name of the branch in which the student studies is :", self.bname)
        print ("The branch code of the branchb in which the student studies is :", self.bcode)
        print("The name of the department which contains both the faculty and the student is: ", self.dname)


class university (department):

    uname = ""

    dno = 0

    def __init__(self, name, year, fname, fsubject, bname, bcode, dname,uname,dno):

        department.__init__ (self, name, year, fname, fsubject, bname, bcode,dname)
        self.uname = uname
        self.dno = dno

    def displayUniversity(self):
        print ("The name of the student is: ", self.name)
        print ("The year of the student is: ", self.year)
        print ("The name of the faculty is: ", self.fname)
        print ("The subject the faculty member above teaches the student is: ", self.fsubject)
        print ("The name of the branch in which the student studies is :", self.bname)
        print ("The branch code of the branchb in which the student studies is :", self.bcode)
        print ("The name of the department which contains both the faculty and the student is: ", self.dname)
        print ("The name of the university which the student studies is: ", self.uname)
        print ("The number of the departments in the university is: ", self.dno)

u=university("Shivesh Pandey",1,"Anuj Mahajan","Programming in Python","Computer Science","CSL 1023","Department Of Engineering","Shri Mata Vaishno Devi University, Kakryal , Katra 182320",8)
u.displayUniversity()
