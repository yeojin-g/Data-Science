import matplotlib.pyplot as plt

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]

y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # [0]*10

for g in grades:
    if g == 100:
        y[9] += 1
    else:
        y[g//10] += 1
    # = y[min(9, g//10)] += 1

print(y) # y = [2, 0, 0, 0, 0, 0, 1, 3, 4, 3]

x = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
x = [i+5 for i in x] #히스토그램 x값 막대 가운데에 오지 않고 양 옆에 위치하도록 x값 위치 5씩 이동


plt.bar(x, y, width=10, edgecolor="black")
plt.xticks([i*10 for i in range(0, 10)]) # 정해진 위치에 각각 x값 지정
plt.show()