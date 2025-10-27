class A:
    varA = "Welcome to class A"
    college = "LPU"
class B:
    varb = "Welcome to class B"
    college= "CGC"
class C(A,B):
    varC = "Welcome to class C"
c1 = C()
print(c1.varA)
print(c1.varb)
print(c1.varC)
print(c1.college)