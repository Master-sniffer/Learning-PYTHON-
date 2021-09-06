import numpy as np
a = np.array([[1,2,4,5,6],[2,4,231,3,5]])
print (a.size)
print (a.itemsize, a.ndim, a.shape)

print (np.tile(a,(2,2)))
