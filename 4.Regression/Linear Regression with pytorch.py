import torch
x = torch.FloatTensor([[1,2], [3,2], [3,7], [1,1], [1,0]])
y = torch.FloatTensor([[4], [8], [23], [1], [-2]])

W = torch.zeros(2,1) # Wx + b -> x가 5x2이므로 W는 2x1이어야함
b = torch.zeros(1,1)

print(W.ndimension())
print(W.shape)
print(x.shape)
# 가설
lr = 0.01
for epoch in range(3001):
    W.requires_grad_(True) #기울기 자동 업데이트
    b.requires_grad_(True)

    h = torch.mm(x, W) + b # 가설 함수
    cost = torch.mean((h - y) ** 2) # mse

    cost.backward() #기울기 구해
    with torch.no_grad(): # W, b 업데이트
        W = W - lr * W.grad
        b = b - lr * b.grad

        if epoch%100:
            print(f"W: {W}, b: {b}, cost: {cost}")
# 지도함수로 W, b를 입력값들을 포함하는 일차함수 그래프의 기울기값과 y절편값으로 설정한 뒤, 아래에서 그 그래프에 값을 넣어보는 것

x_test = torch.tensor([[5,10]], dtype = torch.float)
test_result = torch.mm(x_test, W) + b
#print(test_result.item())
