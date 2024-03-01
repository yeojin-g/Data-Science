import torch

x_train = torch.tensor([[1],[2],[3],[4],[5],[2.5],[3.5],[0],[3.1],[2.7],[2.8],[2.9]], dtype=torch.float)
y_train = torch.tensor([[1],[1],[1],[0],[0],[0],[0],[1],[0],[1],[1],[1]], dtype=torch.float)

W = torch.randn(1,1, requires_grad=True) #입력 차원이 1차원이라서 1x1
b = torch.randn(1,1, requires_grad=True)

optim = torch.optim.SGD([W, b], lr = 1.0) # optimizer
#optim = torch.optim.Adam([W, b], lr = 1.0)
#optim = torch.optim.Adadelta([W, b], lr = 1.0)
#optim = torch.optim.Adagrad([W, b], lr = 1.0)
#optim = torch.optim.RMSprop([W, b], lr = 1.0)

for epoch in range(3001):
    #가설함수
    h = torch.sigmoid(torch.mm(x_train, W) + b) #sigmoid(Wx + b)
    cost = torch.mean(-y_train * torch.log(h) - (1 - y_train) * torch.log(1-h))

    optim.zero_grad() # 기울기 계산 직전에 w,b의 기울기값값 0으 초기화
    cost.backward() # 기울기 계산
    optim.step() # w, b값 갱신

    with torch.no_grad():
        if epoch % 100 == 0:
            print(f"W: {W.item()}, b: {b.item()}, cost: {cost}")

#####################################################
with torch.no_grad():
    x_test = torch.tensor([[4.5],[1.1]], dtype=torch.float)

    h_test = torch.sigmoid(torch.mm(x_test, W) + b)
    h_test[h_test > 0.5] = 1 # 조건에 해당되는 원소만 출력
    h_test[h_test <= 0.5] = 0
    #print(h_test)

#### Matplotlib ####
import matplotlib.pyplot as plt

with torch.no_grad():

    plt.scatter(x_train, y_train) # 점으로 나타내기
    x_tmp = torch.linspace(0,5,100).unsqueeze(1)
    y_tmp = torch.sigmoid(torch.mm(x_tmp, W) + b)
    plt.plot(x_tmp, y_tmp, ":r")
    #plt.show()

#### sklearn ####
from sklearn.linear_model import LogisticRegression

x_train = [[1],[2],[3],[4],[5],[2.5],[3.5],[0],[3.1],[2.7],[2.8],[2.9]]
y_train = [1,1,1,0,0,0,0,1,0,1,1,1]

model = LogisticRegression(penalty='none')
model.fit(x_train, y_train)

print(model.coef_, model.intercept_)

y = model.predict([[4.5],[1.1]])
print(y)