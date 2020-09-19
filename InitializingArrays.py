
import numpy as np

#all 0 matrix - np.zero()
print(np.zeros(5))
print("\n")


# 5x5 with 2 faces
print(np.zeros((2,5,5)))
print("\n")


#all ones matrix

a = np.ones((4,3,3), dtype="int32")

print(a)
print("\n")

#variable/ any other number

b = np.full((2,2), 99)
print (b)
print("\n")

# any other number (full_like)

c = np.full_like(a, 4)
print(c)
print("\n")

#random decimal numbers

print("random")
d = np.random.rand(4,2,3)
print(d)
print("\n")

print("random_sample for shapes")

e = np.random.random_sample(d.shape)
print(e)
print("\n")

#random int values
print("random ints between 0 & 9 ")

f = np.random.randint(0,9, size =(1,3,3))
print(f)

print("\n")
print("array repetition")
print("\n")
arr = f

print("ARR")
print(arr)
print("\n")

print("Repetitions")
r1 = np.repeat(arr,3, axis=0)
print(r1)
print("\n")

#challenge

print("Challenge")

output = np.ones((5,5))
z = np.zeros((3,3))
z[1,1] = 9

output[1:4,1:-1] = z
print(output)