#Matrix Dot Product - 딥러닝 연산 - 행렬곱(가중치곱)
A = np.array([[1,2,3], [4,5,6]])
print(A.shape)
B = np.array([[5,6], [7,8]])
print(B.shape)
C = np.array([[1,2], [3,4], [5,6]])
print(C.shape)

np.dot(A, C) # = np.dot() numpy에서 지원하는 Dot Product 함수
