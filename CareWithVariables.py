
import numpy as np

a = np.array([1,2,3])
b = a

b[0] = 100

print("\nb = a doesnt create a copy of a, it just points calls at b toward a - use array.copy() to create a clone\n")
print("\n print of a:\n")
print(a)
print("\n print of b:\n")
print(b)
#array.copy()


c = np.array([4,5,6])
d = c.copy()

d[0] = 101
print("\nprint of c:\n")
print(c)
print("\nprint of d:\n")
print(d)