import numpy as np

stats = np.array([[1, 2, 3],[4, 5, 6]])

print(stats)

print("\n Basic stats\n")

print("\nCheck minimums/maximums: \n")

print(np.min(stats))

print(np.max(stats))

print(np.min(stats, axis = 1))

print(np.min(stats, axis = 0))

print("\nSum:\n")

print(np.sum(stats))

print("\n Axis 0 refers to the direction 'downward', along the rows\n")

print(np.sum(stats, axis=0))

print("\n axis 1 is the direction along the columns")

print(np.sum(stats, axis=1))



