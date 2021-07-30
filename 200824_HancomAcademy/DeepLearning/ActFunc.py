## Activation Function(활성화 함수) ##
# 활성화 함수의 이용: 러닝에 활용됨.

#1. Step Function 구현 - 그래프 모양이 계단식
import numpy as np
import matplotlib.pylab as plt #딥러닝 라이브러리, 빅데이터 분석용

def step_function(x):
#  if x > 0:
#    return 1
#  else:
#    return 0
# numpy 특성상 위의 방법은 작동하지 않을 수 있음.
  y = x > 0
  return y.astype(np.int) #boolean type 리턴
# astype (y 변수의 데이터타입을 불린 -> 정수형으로 바꾸어 호출함)
X = np.arange(-5.0, 5.0, 0.1) #from -.5 to .5 per .1
print(X)
Y = step_function(X)

plt.plot(X, Y)
plt.ylim(-0.1, 1.1)
plt.show() #계단형으로 그래프가 그려짐: stepfunction인 이유


#2. Sigmoid Function - 그래프 모양이 S를 닮음
def sigmoid(x):
  return 1 / (1 + np.exp(-x)) #numpy에서 제공하는 지수함수

X = np.arange(-5.0, 5.0, 0.1) #from -.5 to .5 per .1
Y = sigmoid(X)

plt.plot(X, Y)
plt.ylim(-0.1, 1.1)
plt.show()


#3. Relu Function - 최근 가장 많이 사용되는 활성화 함수
#입력이 0 초과이면 입력을 그대로 반환, 0 이하이면 0을 반환
def relu(x):
  return np.maximum(0, x)

X = np.arange(-5.0, 5.0, 0.1) #from -.5 to .5 per .1
Y = relu(X)

plt.plot(X, Y)
plt.ylim(-1.0, 5.5)
plt.show()
