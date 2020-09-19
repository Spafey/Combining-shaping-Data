import numpy as np

a = np.genfromtxt('orderedtestdata.csv', delimiter=',')
print(a)
print("\n")

print(a[2:4, 0:2])
print("\n")

print(a[0,1],a[1,2], a[2,3], a[3, 4])

print(a[[0, 1, 2, 3], [1, 2, 3, 4]])+

print("\n")

print(a[[0,4,5], 3:]) # from the 1st, 5th & 6th row of axis 0, return columns 4 & above