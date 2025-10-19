import numpy as np

# for checking the version of numpy
print(np.__version__)

# multiplied the array with 2
array = np.array([[1, 2, 3, 4.99], [5, 6, 7, 8]])
# array = array * 2
print(array)

# to check the dimensions and shape of array
print(array.ndim)
print(array.shape)

# chain indexing
print(array[1][0])
print(array[1, 0])

# arithmetic ops on numbers and concatenation on letters
age = array[0, 1] + array[0, 2]

array2 = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]])

# slicing array[start:end:step]
print(array2[::3])

# accessing column values
print(array2[0, 2])
print(array2[:, 2])  # for accessing all the values from specified column
print(array2[0:2, 2:4])  # selecting only particular rows and columns

# vector arithmetic

print(np.sqrt(array))
print(np.round(array))

array3 = np.array([65, 74, 81, 66, 100])
print(array3 == 100)

##  broadcasting is multiplying/transforming matrices where they can be different dimensions
##  when looking for compatibility, the shape should either match or one of them should be a 1
matrix1 = np.array([1, 2, 3, 4])
matrix2 = np.array([[1], [2], [3], [4]])

print(matrix1 * matrix2)

# aggregate functions
print(np.var(array2))