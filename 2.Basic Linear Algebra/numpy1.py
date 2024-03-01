import numpy as np

a = np.array([1,2,3])
b = np.array([2,3,4])
c = np.zeros() # 0으로 채워진 벡터
d = np.ones([2]) # 1로 채워진 벡터
print(c, d)

print(f"a+b = {a+b}")
print(f"a-b = {a-b}")
print(f"a*b = {a*b}")
print(f"a.dot(b) = {a.dot(b)}")

A = np.array([[1,2,3], [2,3,4]])
B = np.array([[2,3,4], [3,4,5]])

print(f"A+B = {A+B}") # 행렬 더하기
print(f"A-B = {A-B}") # 행렬 빼기
print(f"A.T = {A.T}") # 전치행렬 (Transpose)
print(f"A*B = {A*B}") # 행렬 요소별 곱하기
print(f"A.dot(B.T) = {A.dot(B.T)}") # 행렬 곱하기 / .T = 행렬 뒤집기


