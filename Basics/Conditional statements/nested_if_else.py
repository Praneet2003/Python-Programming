age = int(input("Enter your age: "))
#if age is 18+ and less than 80 then you can drive otherwise not
if(age>=18):
    if(age>=80):
        print("Can't drive.")
    else:
        print("Can drive.")
else:
    print("Can't Drive")
