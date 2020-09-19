
import numpy as np

a = np.array([1, 2, 3, 4])
print(a)
print("\n")

print(a + 2)
print(a - 2)

print("\n")

print(a * 2)
print(a / 2)

print("\n")

b = np.array([1, 0, 1, 0])
print(a + b)

print("\n")

print(" To the nth power")
print(a ** 2)

print("\n Sin:\n")

print(np.sin(a))

print("\n")

print("Cosine:\n")
print(np.cos(a))

###### linear algebra

print("\nLinear Algebra\n")

print("\n Matrix Multiplication - columns of the first matrix must be equal to rows of the second matrix:\n")
a = np.ones((2, 3))
print(a)

print("\n")

b = np.full((3, 2), 2)
print(b)

print("\n")
print(np.matmul(a, b))

print("\n Find the determinant:\n ")

c = np.identity(3)
print(c)
print(np.linalg.det(c))

print("\n Reference docs: (https://docs.scipy.org/doc/numpy/reference/routines.linalg.html) \n")
