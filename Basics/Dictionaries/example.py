info = {
    "name":"Praneet",
    "CGPA": 9.5,
    "Marks": [98,87,89],
    "subjects": ["Math", "Science", "English"]
}
print(type(info))#<class 'dict'>
print(info)# {'name': 'Praneet Raj', 'CGPA': 9.5, 'Marks': [98, 87, 89]}
# Acessing the value of dictionary key
print(info["name"])
# Modifying the name(key) value.
info["name"]= "Praneet Raj"
info["Address"] = "Banka, Bihar"
# Removing items from dictionary.
# Method-1.
info.pop("Marks")
# Method-2.
# del info["CGPA"]
# Method 3.
# info.clear() clears the intire dictionary.
print(info)
#  Looping through dictionary.
# info["CGPA"] = None
print("printing key:Value pairs using loop.")
for key in info:
    print(key," -> ",info[key])