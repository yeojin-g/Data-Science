import numpy
import torch
import torch.nn.functional as F
import torch.nn as nn
x_train = torch.FloatTensor([ [1,2,1,1], [2,1,3,2], [3,1,3,4], [4,1,5,5], [1,7,5,5],
                            [1,2,5,6], [1,6,6,6], [1,7,7,7]])
y_train = torch.tensor([ [0,0,1], [0,0,1], [0,0,1], [0,1,0], [0,1,0], [0,1,0],
                            [1,0,0], [1,0,0]], dtype=torch.float)

W = torch.randn(4, 3, requires_grad=True) # x nx4 y 3x1이니까 W는 4x3인듯
b = torch.randn(1, 3, requires_grad=True) # y때문에 1x3
#optim = torch.optim.Adam([W, b], lr=0.1)
model = nn.Linear(4,3) #W, b 알아서 랜덤하게 초기화
optim = torch.optim.Adam(model.parameters(), lr=0.1)

for epoch in range(3001):
    h = model(x_train)
    #h = torch.mm(x_train, W) + b
    # = (torch.mm(x_train, W).softmax(dim=1)
    cost = F.cross_entropy(h, y_train)
    #cost = -torch.mean(torch.sum(y_train * torch.log(h), dim=1))
    # = -(y_train * torch.log(h)).sum(dim=1).mean()

    optim.zero_grad()
    cost.backward()
    optim.step()

    with torch.no_grad():
        if epoch % 100 == 0:
            print(f"epoch: {epoch}, cost: {cost.item()}")

#############test##############
x_test = torch.tensor([[1,11,10,9],[1,3,4,3],[1,1,0,1]], dtype=torch.float)
h_test = torch.softmax(torch.mm(x_test, W) + b, dim=1)
print(torch.argmax(h_test, dim=1))
print(h_test)

a = torch.tensor([[1,3,2,6,4], [7,2,3,9,8]], dtype=torch.float)
print(torch.argmax(a)) # 전체에서 max값의 인덱스
print(torch.argmax(a, dim=1)) # 1차원에서 각각 max값의 인덱스

#######################################
import numpy as np
from sklearn.linear_model import LogisticRegression

x_train = numpy.array([ [1,2,1,1], [2,1,3,2], [3,1,3,4], [4,1,5,5], [1,7,5,5],
                            [1,2,5,6], [1,6,6,6], [1,7,7,7]])
y_train = numpy.array([2,2,2,1,1,1,0,0])

model = LogisticRegression(penalty='none')
model.fit(x_train, y_train)

x_test = np.array([[1,11,10,9],[1,3,4,3],[1,1,0,1]])

print(model.predict(x_test))