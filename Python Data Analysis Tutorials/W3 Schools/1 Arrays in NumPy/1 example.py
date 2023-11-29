import numpy as np

b = np.empty(2, dtype = int)
print("Matrix b : \n", b)

a = np.empty([2, 2], dtype = int)
print("\nMatrix a : \n", a)

c = np.empty([3, 3])
print("\nMatrix c : \n", c)


#Create Array using numpy.zeros(shape, dtype = None, order = ‘C’)

import numpy as np

b = np.zeros(2, dtype = int)
print("Matrix b : \n", b)

a = np.zeros([2, 2], dtype = int)
print("\nMatrix a : \n", a)

c = np.zeros([3, 3])
print("\nMatrix c : \n", c)


# Operations on Numpy Arrays
# Arithmetic Operations
##  Addition: 


import numpy as np

# Defining both the matrices
a = np.array([5, 72, 13, 100])
b = np.array([2, 5, 10, 30])

# Performing addition using arithmetic operator
add_ans = a+b
print(add_ans)

# Performing addition using numpy function
add_ans = np.add(a, b)
print(add_ans)

# The same functions and operations can be used for
# multiple matrices
c = np.array([1, 2, 3, 4])
add_ans = a+b+c
print(add_ans)

add_ans = np.add(a, b, c)
print(add_ans)


#Subtraction:
import numpy as np

# Defining both the matrices
a = np.array([5, 72, 13, 100])
b = np.array([2, 5, 10, 30])

# Performing subtraction using arithmetic operator
sub_ans = a-b
print(sub_ans)

# Performing subtraction using numpy function
sub_ans = np.subtract(a, b)
print(sub_ans)

#Multiplication:
import numpy as np

# Defining both the matrices
a = np.array([5, 72, 13, 100])
b = np.array([2, 5, 10, 30])

# Performing multiplication using arithmetic
# operator
mul_ans = a*b
print(mul_ans)

# Performing multiplication using numpy function
mul_ans = np.multiply(a, b)
print(mul_ans)

# Division:
import numpy as np

# Defining both the matrices
a = np.array([5, 72, 13, 100])
b = np.array([2, 5, 10, 30])

# Performing division using arithmetic operators
div_ans = a/b
print(div_ans)

# Performing division using numpy functions
div_ans = np.divide(a, b)
print(div_ans)






# NumPy Array Indexing
# Python NumPy Array Indexing
# Python program to demonstrate 
# the use of index arrays.
import numpy as np

# Create a sequence of integers from
# 10 to 1 with a step of -2
a = np.arange(10, 1, -2) 
print("\n A sequential array with a negative step: \n",a)

# Indexes are specified inside the np.array method.
newarr = a[np.array([3, 1, 2 ])]
print("\n Elements at these indices are:\n",newarr)


# NumPy Array Slicing
# Python program for basic slicing.
import numpy as np

# Arrange elements from 0 to 19
a = np.arange(20)
print("\n Array is:\n ",a)

# a[start:stop:step]
print("\n a[-8:17:1] = ",a[-8:17:1])

# The : operator means all elements till the end.
print("\n a[10:] = ",a[10:])


# Python program for indexing using basic slicing with ellipsis
import numpy as np

# A 3 dimensional array.
b = np.array([[[1, 2, 3],[4, 5, 6]],
			[[7, 8, 9],[10, 11, 12]]])

print(b[...,1]) #Equivalent to b[: ,: ,1 ]

# NumPy Array Broadcasting
import numpy as np

macros = np.array([
[0.8, 2.9, 3.9],
[52.4, 23.6, 36.5],
[55.2, 31.7, 23.9],
[14.4, 11, 4.9]
])

# Create a new array filled with zeros,
# of the same shape as macros.
result = np.zeros_like(macros)

cal_per_macro = np.array([3, 3, 8])

# Now multiply each row of macros by
# cal_per_macro. In Numpy, `*` is
# element-wise multiplication between two arrays.
for i in range(macros.shape[0]):
	result[i, :] = macros[i, :] * cal_per_macro

result


import numpy as np

v = np.array([12, 24, 36])
w = np.array([45, 55])

# To compute an outer product we first
# reshape v to a column vector of shape 3x1
# then broadcast it against w to yield an output
# of shape 3x2 which is the outer product of v and w
print(np.reshape(v, (3, 1)) * w)

X = np.array([[12, 22, 33], [45, 55, 66]])

# x has shape 2x3 and v has shape (3, )
# so they broadcast to 2x3,
print(X + v)

# Add a vector to each column of a matrix X has
# shape 2x3 and w has shape (2, ) If we transpose X
# then it has shape 3x2 and can be broadcast against w
# to yield a result of shape 3x2.

# Transposing this yields the final result
# of shape 2x3 which is the matrix.
print((X.T + w).T)

# Another solution is to reshape w to be a column
# vector of shape 2X1 we can then broadcast it
# directly against X to produce the same output.
print(X + np.reshape(w, (2, 1)))

# Multiply a matrix by a constant, X has shape 2x3.
# Numpy treats scalars as arrays of shape();
# these can be broadcast together to shape 2x3.
print(X * 2)


