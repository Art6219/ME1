import numpy as np

a = np.array([[1, 2], [3, 4]])

b= np.zeros((4, 4))

b[2:4,2:4] = a.copy()

print(b)