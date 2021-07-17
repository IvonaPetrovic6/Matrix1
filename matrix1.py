x = int(input("Number of rows: "))
y = int(input("Number of columns: "))
print("Add elements: ")

matrix = ""

for i in range(x):
    for j in range(y):                 # adding elements to matrix row by row
        matrix += input("> ")

k = 0                                  # starting from 0 element of matrix

for i in range(x):
    for j in range(y):                 # printing matrix elements
        print(matrix[k],end = " ")
        k += 1
    print("")
