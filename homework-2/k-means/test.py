
import numpy as np

a = [[np.array([1,2]),3] for _ in range(10)]

a = np.array(a,dtype=object)
b = np.array(a[:,0],dtype=object)
b = b[:,[0]]
print(b.shape)
