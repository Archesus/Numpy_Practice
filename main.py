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

array3 = np.array([65, 74, 81, 66, 100, 50, 55, 61])
print(array3 == 100)

##  broadcasting is multiplying/transforming matrices where they can be different dimensions
##  when looking for compatibility, the shape should either match or one of them should be a 1
matrix1 = np.array([1, 2, 3, 4])
matrix2 = np.array([[1], [2], [3], [4]])

print(matrix1 * matrix2)

# aggregate functions
print(np.var(array2))
print(np.argmax(matrix1))

# we can sum the columns or rows using the axis parameter
matrix3 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(np.sum(matrix3, axis=1))

# filtering is selecting values/elements on the basis of some conditions
passed = array3[array3 > 70]
just_passed = array3[(array3 >= 50) & (array3 < 70)]
even_scores = array3[array3 % 2 == 0]
print(passed)
print(just_passed)
print(even_scores)


# random numbers/variable
rng = np.random.default_rng()
# print(rng.integers(low, high, (shape, shape)))
print(rng.integers(1, 1000, (2, 2)))

print(np.random.uniform())

rng_shuffle = np.random.default_rng()
rng_shuffle.shuffle(matrix1)  # shuffling the numbers in an array
print(matrix1)

random_choice = rng_shuffle.choice(matrix1)  # choosing random number from the array
print(random_choice)  