student = {
    "name":"Praneet Raj",
    # "subjects": ["Math", "Science", "English"]
    # here in above line we have only subjects but we want to have suject and it's corresponding marks to it.
    #  so we will use the nested dictionary for this.
    "subjects":{
        "Maths":98,
        "Science": 89,
        "English":{
            "Eng1":89,
            "Eng2":93
        }
    }
}
print(type(student))
print(type(student["subjects"]))
print(student["subjects"])
print(student["subjects"]["Maths"])# we want to print subject in which we have to print Maths marks.
print(student["subjects"]["English"]["Eng1"])# we want to print subject in which we have to print English marks -> Eng1.
print(student.keys())
print(student["subjects"].keys())
print(student["subjects"]["English"].keys())
#  to find numbers of keys in dictionary
print(len(student))
print(student.keys())# print all the keys of the dictionary. dict_keys(['name', 'subjects'])
print(student.values())#prints all the values of the dictionary.  dict_values(['Praneet Raj', {'Maths': 98, 'Science': 89, 'English': {'Eng1': 89, 'Eng2': 93}}])
print(student.items())#print all key:value pairs.  dict_items([('name', 'Praneet Raj'), ('subjects', {'Maths': 98, 'Science': 89, 'English': {'Eng1': 89, 'Eng2': 93}})])
student.update({"Roll no": 51,
                "Address":"Bihar"})
print(student)