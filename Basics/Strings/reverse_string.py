str = input("Enter a String: ")
def reversestr(str):
    rev = "".join(reversed(str))
    return rev
def reversestr2(str):
    reversed=""
    for i in range(len(str)-1,-1,-1):
        reversed += str[i]
    return reversed
def reversestr3(str):
    reversed = str[::-1]
    return reversed
print(reversestr(str))
print(reversestr2(str))
print(reversestr3(str))