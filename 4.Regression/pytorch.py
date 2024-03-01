import torch
x = torch.tensor([[1,2,3], [4,5,6], [7,8,9]]) # 자동으로 int형 텐서 생성
xx = torch.tensor([[1.0,2,3], [4,5,6], [7,8,9]]) # 자동으로 float형 텐서 생성 - 1.0때문
xxx = torch.tensor([[1,2,3], [4,5,6], [7,8,9]], dtype=torch.float) # 타입을 float으로
y = torch.FloatTensor([[1,2,3], [4,5,6], [7,8,9]]) # 타입을 float으로 정해
print("x = ", x, " Type x: ", x.type())

# 텐서 모양 알아보기
print(x.shape) # = x.size()

# rank 알아보기 - 차원
print(len(x.shape))
print(x.ndimension()) # = x.ndim

# 텐서 모양 바꾸기
# unsqueeze -> 차원(rank)늘리기
x0 = torch.unsqueeze(x, 0)
x1 = torch.unsqueeze(x, 1)
x2 = torch.unsqueeze(x, 2)
xList = [x0, x1, x2]
for i in xList:
    print(i)
    print(i.shape)

# squeeze -> 차원 크기 1인 차원 제거
x00 = torch.squeeze(x0)
print(x00)
print(x00.shape)

# view
xView9 = x.view(9) # x.view(8) = error
xView1 = x.view(1,3,-1) # -1 두 군데는 못써
print(xView9)
print(xView9.shape)
print(xView1)
print(xView1.shape)

# 행렬 연산
x = torch.tensor([[1,2], [3,4], [5,6]], dtype=torch.float)
w = torch.randn(1,2) #평균이 0, 표준편차가 1인 랜덤 정수 채워줘 // 1x2 matrix
b = torch.randn(3,1) # dtupe default = torch.float // 3x1 matrix
print(x)
print(w)
print(b)

# x * w + b
result = torch.mm(x, torch.t(w)) + b # matrix multi = mm // .t() = 행렬 뒤집기
print((x * w).sum(axis=0).view(2, 1))
print(result)

# 기울기 계산
w = torch.tensor(1.0, requires_grad=True)
a = w*3
l = a**2
l.backward() # 기울기 계산
print("l을 w로 미분한 값: ", w.grad)