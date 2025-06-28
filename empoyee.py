class Person:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    
    def display(self):
        print("the name of the person is",self.name)
        print('the name of the id is',self.id)
class Employee(Person):
    
    def __init__(self,name,id,post,salary):
        self.post=post
        self.salary=salary
        Person.__init__(self,name,id)
obj=Employee("Rahul","B101","Engineer","$130,000")
obj.display()