num = int(input("Enter the nth no: "))
def fibo(num):
    lst = list()
    a=0
    b=1
    if(num==0):
        lst.append(a)
        return lst
    if(num==1):
        lst.append(b)
        return lst
    for _ in range(2,num+1):
        a,b = b,a+b
    lst.append(b)
    return lst
print(fibo(num))