import numpy as np

a = np.array([[1, 2], [3, 4]])

a[0] = np.zeros(len(a[0]))

print(a)