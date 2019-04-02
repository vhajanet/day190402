import numpy as np

#a = np.arange(12).reshape(-1,4)
#print(a)

#print(a[[0,1]])
#print(a[[1,0]])

#print(a[[1,0],[0,1]])

#연습)
#테두리가 1로 채워지고 속은 0으로 채워진 5*5배열을 만들어봅니다.
#indexArray를 이용해 봅니다.

#a = np.arange(25).reshape(5,5)
#print(a)

#b= np.zeros(25).reshape(5,5)
#print(b)
#c = np.zeros_like(b[1:4,1:4])
#print(c)

#print(b)
#b[:,[0,-1]]=1
#b[[0,-1]] =1
#print(b)

#연습)
#0으로 채워진 5*5 배열을 만들고 대각선을 1로 만드세요
#
a = np.zeros(25).reshape(5,5)
#print(a)
#a[3:1]=1
a[1,1]=1
a[2,2]=1
a[3,3]=1
a[4,4]=1
print(a)