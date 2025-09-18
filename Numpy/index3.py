import numpy as np 
x=np.array([1,2,3,4])
print("Array is :",x)
print("New Array is :",x[1:3])# Slicing :includes 1st but not 3rd index
print(x[1:2:3])# print an array other than 3 from 1st to 2nd index 
print(x[::2])
#Slicing in 2D array
y=np.array([[1,2,3,4],[5,7,8,9]])
print(y[1,1:3])
print(y[0:2, 2])
print(y[1:2,1:3])