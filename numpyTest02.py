import numpy as np

a = [1,2,3,4,5]
b = [1.0, 2.0, 3.0, 4.0, 5.0]
c = ['a','b','c','d','e']
d = ['hello','java','python','oracle','mongo']
e = ['김경민','오상훈','이성기','김도희','정연미']

arr1 = np.array(a)
arr2 = np.array(b)
arr3 = np.array(c)
arr4 = np.array(d)
arr5 = np.array(e)

print(arr1.dtype)
print(arr2.dtype)
print(arr3.dtype)
print(arr4.dtype)
print(arr5.dtype)