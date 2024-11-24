import numpy as np

# Create two matrices
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Display the matrices
print("Matrix 1:")
print(matrix1)
print("\nMatrix 2:")
print(matrix2)

# Add the matrices
matrix_sum = np.add(matrix1, matrix2)
print("\nSum of Matrix 1 and Matrix 2:")
print(matrix_sum)

# Multiply the matrices element-wise
matrix_product = np.multiply(matrix1, matrix2)
print("\nElement-wise Product of Matrix 1 and Matrix 2:")
print(matrix_product)

# Perform matrix multiplication
matrix_dot_product = np.dot(matrix1, matrix2)
print("\nMatrix Multiplication (Dot Product) of Matrix 1 and Matrix 2:")
print(matrix_dot_product)

# Transpose of Matrix 1
matrix_transpose = np.transpose(matrix1)
print("\nTranspose of Matrix 1:")
print(matrix_transpose)

# Create a new matrix for row-wise and column-wise operations
matrix3 = np.array([[1, 2, 3], 
                    [4, 5, 6], 
                    [7, 8, 9]])

print("\nMatrix for Row-wise and Column-wise Operations:")
print(matrix3)

# Row-wise sum (sum along axis 1)
row_wise_sum = np.sum(matrix3, axis=1)
print("\nRow-wise Sum:")
print(row_wise_sum)

# Column-wise sum (sum along axis 0)
column_wise_sum = np.sum(matrix3, axis=0)
print("\nColumn-wise Sum:")
print(column_wise_sum)

#Output

Matrix 1:
[[1 2]
 [3 4]]

Matrix 2:
[[5 6]
 [7 8]]

Sum of Matrix 1 and Matrix 2:
[[ 6  8]
 [10 12]]

Element-wise Product of Matrix 1 and Matrix 2:
[[ 5 12]
 [21 32]]

Matrix Multiplication (Dot Product) of Matrix 1 and Matrix 2:
[[19 22]
 [43 50]]

Transpose of Matrix 1:
[[1 3]
 [2 4]]

Matrix for Row-wise and Column-wise Operations:
[[1 2 3]
 [4 5 6]
 [7 8 9]]

Row-wise Sum:
[ 6 15 24]

Column-wise Sum:
[12 15 18]