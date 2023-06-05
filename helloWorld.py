print("Hello World")
class Employee:
    def __init__(self,fname,lname,pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = self.fname + self.lname +"@gmail.com"

    def full_name(self):
        return self.fname + " " + self.lname
    
emp1 = Employee("Avinash","K",900000)
print(emp1.full_name())