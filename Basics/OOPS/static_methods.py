class Student:
    @staticmethod
    def college():
        print("LPU")
    def __init__(self,name):
        self.name = name
    def getdetails(self):
        print(self.name)
        self.college()
s1 = Student("Praneet Raj")
s1.getdetails() 
Student.college()