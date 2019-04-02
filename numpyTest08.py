import numpy as np
# 결론
# 차원이 다른 것 끼리 연산이 가능하려면
#

#a = np.arange(3)
#b = np.arange(6)

#c = a + b
#print(c)


a = np.arange(3) # [0,1,2]
b = np.arange(6)
c = np.arange(3).reshape(-1,3) #[[0,1,2]]
d = np.arange(6).reshape(-1,3) #[0,1,2,3,4,5,6] / [[0,1,2] [3,4,5]]
e = np.arange(3).reshape(3,-1) #[[0],[1],[2]]

#print(a)
#print(b)
#print(c)
#print(d)
#print(e)

#print(a+b)  # 오류ValueError: operands could not be broadcast together with shapes (3,) (6,)
#print(a+c)  # vector operation [[0 2 4]]

#print(a+d)   # [[0 2 4] [3 5 7]]
# a는 1차원 배열이고
# b은 2차원배열끼리 연산을 수행하였더니
# a배열의 b배열의 행만큼 연산을 수행 ====> broad Casting
# a배열의 요소 하나하나가 b배열의 각 행의 열과 대응하여 연산 ====> vector

#print(a+e) # [[0 1 2] [1 2 3] [2 3 4]] vectorOperation, VectorOperation

#print(b+c) # ValueError: operands could not be broadcast together with shapes (6,) (1,3)

#print(b+d) # ValueError: operands could not be broadcast together with shapes (6,) (2,3)

#print(b+e) # [[0 1 2 3 4 5] [1 2 3 4 5 6] [2 3 4 5 6 7]]

#print(c+d) # [[0 2 4] [3 5 7]]
print(d+e) #

