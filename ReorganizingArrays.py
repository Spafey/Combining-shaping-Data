
import numpy as np

print("\n Reshaping arrays\n")
before = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(before.shape)
print(before)

print("\n")

print("\n")

after = before.reshape((8, 1))
print(after.shape)
print(after)

print("\n")

print(after.shape)
print(after.reshape((4, 2)))

print("\n")

print(after.shape)
print(after.reshape((2, 2, 2)))

print("Changing the underlying variables")

after = after.reshape((2, 2, 2))
print(after.shape)

after = after.reshape((2, 4))
print(after.shape)

after = after.reshape((1, 8))
print(after.shape)

after = after.reshape((4, 1, 2))
print(after.shape)
print("\n")

print(after)

print("\n vertically Stacking vectors\n")

v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])

print(np.vstack([v1, v2]))

print("\n")


stack = np.vstack([v1, v2, -v1, -v2])

print(stack)

print("\n Horizontal stack:\n")

h1 = np.ones((2, 4))
h2 = np.zeros((2, 2))

h = np.hstack((h1, h2))
print(h)
