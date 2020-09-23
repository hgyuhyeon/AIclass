#Nerual network (인공 신경망) 구현 - deep layer 구조

#perceptron 1st layer
X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3 ,0.5], [0.2, 0.4 ,0.6]]) #weight of perceptron
B1 = np.array([0.1, 0.2, 0.3]) #bias per perceptron
print("1st layer")
print(W1.shape) #(2, 3)
print(B1.shape) #(3, )
print(X.shape) #(2, )
A1 = np.dot(X, W1) + B1 #DotProduct 연산(가중치곱 연산, X와 W1) + B1 값 더함
print(A1) #[0.3, 0.7, 1.1] => 각 a1, a2, a3은 활성화 함수에 들어갈 input values
Z1 = sigmoid(A1) #convert A1 to Z1 (for next layer)
print(A1)
print(Z1) #[0.5, 0.6, 0.7]

#perceptron 2nd layer
W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
B2 = np.array([0.1, 0.2])
print("\n2nd layer")
print(Z1.shape) #(3, )
print(W2.shape) #(3, 2)
print(B2.shape) #(2, )
A2 = np.dot(Z1, W2) + B2
Z2 = sigmoid(A2)
print(Z2) #same as 1st layer

#output layer
def identity_function(x): 
  return x
W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
B3 = np.array([0.1, 0.2])
A3 = np.dot(Z2, W3) + B3
Y = identity_function(A3) #or Y = A3, 항등함수
print("\noutput layer") #same as 1st, 2nd layer
print(Y)

# ex) 개 고양이 분류 모델 구현일 때
# 1st layer input으로 들어온 사진이 개일 확률
# 2nd layer input으로 들어올 사진이 고양이일 확률일 때
# input으로 들어온 사진은 두 번째 perceptron의 값이 더 크다면 무엇일까?
# -> 고양이
# 왜: 구조 변경 없이 Weight와 bias값만 바뀌므로 .... 근데 난 잘 이해가 안 가;;
