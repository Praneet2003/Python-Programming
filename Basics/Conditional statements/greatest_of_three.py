a,b,c = map(int,input("Enter three numbers: ").split())
def checkodd(num):
    if(num%2==0):
        return "Even"
    else:
        return "Odd"
def greatest(a,b,c):
    if(a>b and a>c):
        print(a,"A is Greatest.")
        print(checkodd(a))
    elif(b>a and b>c):
        print(b,"B is Greatest.")
        print(checkodd(b))
    else:
        print(c,"C is Greatest.")
        print(checkodd(c))
greatest(a,b,c)