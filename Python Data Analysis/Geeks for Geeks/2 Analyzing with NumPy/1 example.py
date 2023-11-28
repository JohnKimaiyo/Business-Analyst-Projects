# creating an array
import numpy as np

b = np.empty(2,dtype = int)
print("Matrix b:\n",b)

a = np.empty([2,2],dtype = int)
print("\nMatrix b:\n",a)

c = np.empty([3,3])
print("\nMatrix c: \n",c)

# create Array using numpy zero 

import numpy as np
b = np.zeros(2,dype = int)
print('Matrix b : \n',a)

a = np.zeros([2,2],dtype = int)
print("\nMatrix a: \n",a)

c = np.zeros([3,3])
print('\nMatrix c:\n',c)


# Operations on Numpy 

# Aritmetic Operations

# Additon

import numpy as np

# Defining both the matrices

a = np.array([5,72,13,100])
b= np.array([2,5,10,30])

# Perfomring addition using arithmetic operaator
add_ans = a + b
print(add_ans)

# Performing addition using numpy function
add_ans = np.add(a,b)
print(add_ans)

# The same functions and operations can be used for
# muliple matrices

c = np.array([1,2,3,4])
add_ans = a + b + c
print(add_ans)

add_ans = np.add(a,b,c)
print(add_ans)      

 # subtraction
 import numpy as np
 
 # defining both the matrices
 a = np.array([5,72,13,100])
b= np.array([2,5,10,30])

# performing subtraction using arithmetci operator
sub_ans = a-b
print(sub_ans)

# perfomring subtraction using numpy function
sub_ans = np.subtract(a,b)
print(sub_ans)