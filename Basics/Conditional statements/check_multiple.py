num = int(input("Enter a number: "))
def checkmultiple(num):
    if(num%7==0):
        return True
    else:
        return False
print(checkmultiple(num))