import numpy as np

a = [1,3,0,3,1]
#연습)
#a배열의 요소만큼의 행의 크기를 갖고 a배열의 요소중에 최대값의 열의 크기를 갖는
#0으로 채워진 2차원 배열을 만들고
#각 행마다 a배열의 요소에 해당하는 열에 1을 채웁니다.
'''
0   1   0   0
0   0   0   1
1   0   0   0
0   0   0   1
0   1   0   0
'''
#b = np.zeros(20).reshape(5,4)
#b = np.zeros([len(a),np.max(a)+1],dtype="int32")
#b[[range(5)],a] =1
#b[[0,1,2,3,4],[a[0],a[1],a[2],a[3],a[4]]]=1
#print(b)

b = np.eye(len(a),np.max(a)+1,dtype='int32')[a]
print(b)