class Employee:
    def __init__(self,fname,lname,pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = self.fname + self.lname +"@gmail.com"

    def full_name(self):
        print(self.fname + " " + self.lname)

    @staticmethod #just a normal function with out no automatic first arg
    def randompay():
        print("hi i am random , not related to self and class ")

emp1 = Employee("Avinash","K",90000)

class Manager(Employee):
    def __init__(self, fname, lname, pay,manager_emp=None):
        super().__init__(fname, lname, pay,manager_emp)
        self.manager_emp = manager_emp

        if self.manager_emp  is not None:
            self.manager_emp = manager_emp
        else:
            self.manager_emp = []
        for emp in self.manager_emp:
            print(emp.full_name())

manager1 = Manager("Suresh","manik",120000,[emp1])