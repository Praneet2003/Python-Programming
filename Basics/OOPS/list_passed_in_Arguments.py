class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def average(self):
        sum =0
        count=0
        for i in self.marks:
            sum+=i
            count+=1
        return sum/count
s1 = Student("Praneet Raj",[97,58,93,95])
print("Student average is: ",s1.average())