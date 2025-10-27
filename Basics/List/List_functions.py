lst = [1,2,3]
lst.append(4)
lst.append(4)
lst.insert(4,5)# inserting 5 at index 4
lst2 = [6,7]
lst.extend(lst2)#add all elements of lst2 in lst.
print("Occurence of 4: ",lst.count(4))
lst.append("hello world")
lst.reverse()
print("hello world" in lst)# checking wheter hello world is present in list or not.
print(lst)
lst.remove("hello world")
print(lst)
print("Popped Element: ",lst.pop(2))
lst.sort(reverse=True)
print(lst)
lst.reverse()
print(lst)
def checksorted(lst):
    for i in range(0,len(lst)-1,1):
        if(lst[i]>lst[i+1]):
            return False
    return True
print(checksorted(lst))