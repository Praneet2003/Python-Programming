lst = list(map(str,input("Enter elements of the list: ").split()))
lst1 = lst.copy()
lst1.reverse()
print(lst1==lst)
# Enter elements of the list: 1 abc bca 1
# False