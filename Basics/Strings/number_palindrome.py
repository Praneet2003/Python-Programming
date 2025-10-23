def reverse(num):
    rev =0
    while(num>0):
        rem = num%10
        rev=rev*10+rem
        num//=10
    return rev
num = int(input("Enter a number: "))
print(reverse(num))
print(num==reverse(num))