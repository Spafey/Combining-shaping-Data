
import numpy as np

a = np.genfromtxt('testdata.csv', delimiter=',')
print(a)

print("\n Boolean expressions - e.g., numbers > 3 \n")

print(a > 3)

print("\nIndexing (Greater than 3)\n")

b = a[a > 3]
print(b)

print("\n You can index with a list in numpy:\n")

c = np.array([1, 2, 3, 4, 5, 6, 7])
print(c[[0, 1, 2, 6]])

print("\n check if ANY number in a row is (greater than 3) & return bool:\n")

d = np.any(a > 3, axis=0)
print(d)

print("\nCheck if ALL numbers in a column are (greater than 2) & return a bool:\n")

e = np.all(a > 2, axis=1)
print(e)

print("\n Multiple rules - Above or below 3\n")

f = (a > 3) | (a < 3)
print(f)



