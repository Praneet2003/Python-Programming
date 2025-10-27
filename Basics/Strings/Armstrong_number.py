num = int(input("Enter a no: "))
orig = num
length = len(str(num))
sum=0
while(num>0):
    rem = num%10
    sum+=rem**length
    num//=10
print(orig==sum)