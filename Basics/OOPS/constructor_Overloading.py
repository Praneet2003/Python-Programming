class Student:
    collegename = "LPU"
    name = "Unknown"
    def __init__(self,fullname=None):
        if(fullname==None):
            self.name = name#instance varibale which is different for all objects.
            print("Defalut constuctor called.")
        else:
            self.name = fullname
            print("Parameterized constructor called.")
    def getdetails(self): 
        print("Student name: ",self.name)
        print("Student's college name: ",self.collegename)
s1 = Student()
s1.getdetails()
s2 = Student("Praneet Raj")
s2.getdetails()