import numpy as np
matrix = []
row = int(input("Enter the number of rows of array: "))
col = int(input("enter the number of columns of array: "))
for i in range(row):
    a=[]# for each value of i , new list a will be created
    for j in range(col):
        val= int(input())
        a.append(val)
    matrix.append(a)
    # after each itteration of i , the value of a will be appended to the matrix.
print("Printing the elemnts of mattrix given by the user is: ")
for i in range(row):
    for j in range(col):
        print(matrix[i][j],end = ' ')
    print()