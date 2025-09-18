import numpy as np
x=np.array([1,5,3,2])
print("The value of an array at index 3 is:",x[3])
print("The sum of two different elements in an array is :",x[1]+x[2])
y=np.array([[1,2,3],[4,5,6]])
print("The 2nd row of the matrix is :",y[0,1]) #y[row,cols]
z=np.array([[[1,2,3],[3,4,5]],[[6,7,8],[9,0,10]]])
print(z[0,1,-1])
