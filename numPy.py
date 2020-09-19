import numpy as np

#test
l = [1, 2]
nplist = np.array(l)
print(nplist)
print("\n")

#declaring arrays
a = np.array([1,2,3], dtype='int32')
print(a)
print("\n")

b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]], dtype='int16')# returns as int
print(b)
print("\n")

#dimension/shape/type/size/total size - not working

print(" to show features of arrays: \n")

#get number of dimensions
print(a.ndim)

#get shape
print(b.shape)

#get type
print(a.dtype)

#get size
print(a.itemsize)

#get total size
print(a.nbytes)


