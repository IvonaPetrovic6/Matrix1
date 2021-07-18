x = int(input("Number of rows: "))
y = int(input("Number of columns: "))
print("Add elements: ")

matrix = ""

for i in range(x):
    for j in range(y):
         matrix += input("> ")          # adding elements to matrix row by row
         matrix += " "

matrix1 = matrix.split(" ")              # splitting elements where there is " "

k = 0                                    # starting from 0 element of matrix

for i in range(x):
    for j in range(y):                   # printing matrix elements
        print(matrix1[k], end = " ")
        k += 1
    print("")

k = 1                                    # starting from element 1
max = matrix1[0]                         # assuming 0 element is the largest one

for i in range(x):
    for j in range(y):
        if matrix1[k] > max:             # comparing other elements with 0 element
            max = matrix1[k]
        k += 1

print(f"The largest number in this matrix is {max}.")