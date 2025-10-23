str = "python programming"
print(len(str))
print(str.capitalize()) 
print(str.endswith('ng'))
print(str.replace('o','O')) # replace all o present in the string with O.
print("first index of o in string is: ",str.find('o'))# returns 1st index of 1st occurence.
print(str.count('mm'))
print(str)
print("".join(["hello ","world ","i am ","praneet"]))
print(str.split())
a = 2.45667
print("float upto 2 places using format(): {:.2f}".format(a))
print(f"float upto 2 places using f-string: {a:.2f}")
print("float upto 2 places using (%%.2f) is:  %.2f"%a)
print("string printed using %%s is: %s"%str)