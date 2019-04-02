import numpy as np

#a = np.ones([5,5],dtype='int32')
#a[1:4,1:4] = 0
#print(a)

a = np.arange(12).reshape(-1,4)
#print(a)

for i in range(4):
    print(a[:,i])

