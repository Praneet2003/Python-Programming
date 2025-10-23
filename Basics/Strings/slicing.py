str = input("Enter a String: ")
print(len(str))
print(str[1:4])
print(str[1:],"str[1:] is same as str[1:len(str)] "+str[1:len(str)])
print(str[:4],"str[:4] is same as str[0:4] ",str[0:4])
print(str[:])
#Output: 
# Enter a String: Apna Banka
# 10
# pna
# pna Banka str[1:] is same as str[1:len(str)] pna Banka
# Apna str[:4] is same as str[0:4]  Apna