class Employee:
    def __init__(self,fname,lname,pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = self.fname + self.lname +"@gmail.com"

    def full_name(self):
        return self.fname + " " + self.lname
    
    @staticmethod #just a normal function with out no automatic first arg
    def randompay():
        print("hi i am random , not related to self and class ")