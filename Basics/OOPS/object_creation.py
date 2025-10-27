class Student:
    name = "Praneet"
    def __init__(self):
        print("This is a constructor")
    def __init__(self,fullname):#parameterized constructor.
        print("This is the constructor of Student class")
        self.name = fullname
    def getdetails(self):
        print("Student details.")
        print("Name: ",self.name)
s1 = Student("Praneet Raj")
# print(s1.name)
# s1.getdetails()
# s2 = Student("Anshu Kumar Chourasia")
s2 = Student()
print(s2.name)