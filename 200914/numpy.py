import numpy as np
#using colab

def printinfo(array):
  print("shape: {}, dimension: {}, dtype: {}"
  .format(array.shape, array.ndim, array.dtype))
#shape = 형태((2,3) 등), ndim = 차원, dtype = 데이터 타입

data = [[1,2,3],[4,5,6]] #numpy를 이용, 간단한 배열 만들기
nparr = np.array(data, dtype = float)
print(nparr)
printinfo(nparr)

#np.zeros
array = np.zeros(5) 
#지정된 크기만큼 배열 생성, 모든 요소는 0.0으로 초기화
#생성 시 float타입으로 생성됨, 출력시 0.0
print(array)
printinfo(array)
array = np.zeros((3,4)) #특정 shape 지정
print(array)
printinfo(array)

#np.ones
array = np.ones((3,4)) #모든 요소를 1.0으로 초기화
print(array)
printinfo(array)

#np.full
array = np.full((3,4), 1234) #인자2개, shape / 초기화할 값
print(array)
printinfo(array)

#np.empty
array = np.empty((4,2)) #요소를 초기화하지 않은 상태로 배열 생성
print(array)
printinfo(array)

#np.eye
array = np.eye(4) #정사각형의 대각행렬
print(array)
printinfo(array)

#np.arange
array = np.arange(24) #0부터 23까지 순서대로 원소 배정
print(array)
reshape_array = np.reshape(array, (4,6)) #배열을 특정 shape 형태로 변환, 차원은 유지된다.
print(reshape_array)
a = np.arange(1,10).reshape(3,3) #1~9까지, 형태 3x3, 차원은 1
print(a)
b = np.arange(9,0,-1).reshape(3,3) #9~1까지, 형태 3x3, 차원은 1
print(b)
np_a = np.arange(1000000)
print(np_a)
%time np_a + 1
#코드 실행 시 해당 명령어가 수행되는 데 걸리는 시간을 측정해 줌(파이썬)
python_a = range(1000000) #파이썬의 range함수로 실행 시 numpy에 비해 오래 걸림
print(python_a)
%time [i+1 for i in python_a]

#np.linspace
a = np.linspace(0, np.pi, 9).reshape(3,3) 
#특정 구간에서 지정된 개수 만큼의 값을 생성
#인자: start, end, 개수
print("np.pi = ", np.pi)
print(a)
