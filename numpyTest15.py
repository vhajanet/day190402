import numpy as np
#연습)
name = ['홍길동','강감찬','이순신','유관순','박주호']
score = [80,90,100,70,95]

np.argwhere(score == np.argmax(score))


#arr1 = np.array(score)
#r = np.max(arr1)
#print(r)
#idx = np.argmax(arr1)
#print(idx)
#print(name[idx])


#a = [4,3,1,5,2]
#arr1 = np.array(a)
#r = np.max(arr1)
#idx = np.argmax(arr1)
#print(r)
#print(idx)

#연습)
#name = ['홍길동','강감찬','이순신','유관순','박주호','김경민','문재인']
#score = [80,90,100,70,100,95,100]

#성적순으로 이름을 출력해 봅니다.

#arr_name = np.array(name)
#arr_score = np.array(score)

#a = np.argsort(arr_score)[::-1]
#[3,0,1,4,2]
#[2,4,1,0,3]
#print(a)
#print(arr_name[a])