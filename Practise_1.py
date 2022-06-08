# classes   - blueprint to logically group data and build upon
# objects   - instance of class
# methods   - any functions or procedures in a class
# attribute - any data in a class

class Student:
    def __init__(self, name, batch):    #instance method
        self.name = name
        self.batch = batch

    def changeSession(self):
        self.batch += 1
        
student1 = Student('John', '5A')

print(student1.changeSession)
