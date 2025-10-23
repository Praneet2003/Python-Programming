def reverse(str):
    rev = "".join(reversed(str))
    return rev
def reverse2(str):
    rev = ""
    for i in range(len(str)-1,-1,-1):
        rev+=str[i]
    return rev
str = input("Enter String to check palindrome: ")
print(str==reverse2(str))