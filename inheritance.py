class animal:
    name=""
    gender=""
    colour=""
    noise=""
    type=""
    height=0
    weight=0
    def __init__(self,n,g,c,no,t,h,w):
        self.name = n
        self.gender = g
        self.colour = c
        self.noise = no
        self.type = t
        self.height = h
        self.weight = w
    def makenoise(self):
        print("No Noise")
class cat(animal):
    domestic_type=""
    stripes_pattern=""
    def __init__(self,n,g,c,no,t,h,w,d_t,s_p):
        animal.__init__(self,n,g,c,no,t,h,w)
        self.domestic_type = d_t
        self.stripes_pattern = s_p
    def makenoise(self):
        self.noise="Meowwwwwwwwwwwwwwwwwwwww Meowwwwwwwwwwwwwwwwwwwwwww"
        print("The cat makes the sound: ",self.noise)
    def display(self):
        print("The name of the cat is: ",self.name)
        print ("The gender of the cat is: ", self.gender)
        print ("The colour of the cat is: ", self.colour)
        print ("The breed of the cat is: ", self.type)
        print ("The height of the cat is: ", self.height)
        print ("The weight of the cat is: ", self.weight)

c=cat("tom","male","grey","meowwwwwwwwwww","siamese",12,234,"Domestic","NO STRIPES")
c.display()
c.makenoise()


