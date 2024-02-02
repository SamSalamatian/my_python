import numpy as np 
import matplotlib as plt
import sys

"""
a = np.array ([[1,2,3,4,5,6,7,8],[9,10,11,12,13,14,15,16]],dtype="int16")
print (f"a dimentison is: {a.ndim}")
print (f"a shape is: {a.shape}")
print (f"a shape is: {a.dtype}")
print (f"a size is: {a.itemsize}")
print (f"a ?size is: {a.size}")
print (f"a total bytes is: {a.nbytes}")s
#caling an item:
print(a[0,3])
#changing an item
a[0,3]= 44
print(a[0,3])
#slicing a[row,column,step] slicing format: [startindex,endindex,step]
print (a[0,1:7:2])
#changing a whole part of array:
a[1,1:3]=5
print(a[1,1:3])
a[1,1:3]=[0,0]
print(a[1,1:3])
print(a)

#Numpy Mathematics is the same as python:
b = np.array([[1,2],[0,3]])
b += 2
print (b)

b -= 2
print (b)

b *= 2
print (b)

b= b / 2
print (b)

b **= 2
print (b)
"""
#Linear Algebra
c = np.zeros((2,2))
print (c)
d = np.ones((4,5))
print (d)
e = np.full((3,3),4)
print (e)

#dot multiplication
#c = np.dot(a,b)
#print(c)

