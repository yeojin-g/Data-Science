f = open("fb.txt", "r")

edges = []

for line in f:
    edges.append(tuple(int(x) for x in line.split()))

f.close()

num_friends = {}

for (u, v) in edges:
    if u not in num_friends:
        num_friends[u] = 0
    if v not in num_friends:
        num_friends[v] = 0

    num_friends[u] += 1
    num_friends[v] += 1

print(num_friends)

# 평균 (mean)
mean = sum(num_friends.values()) / len(num_friends)
print(f"mean: {mean}")

# 중앙값 (median)
num_friends_list = sorted(num_friends.values())
median = num_friends_list[len(num_friends_list) // 2]
print(f"median: {median}")

from collections import Counter

# 최빈값 (mode) - 방법 2개
mode = Counter(num_friends_list).most_common(1)[0]
print(mode)
print(f"mode {mode}")

# 최대값, 최소값
min = min(num_friends_list)
max = max(num_friends_list)

print(f"min: {min}, max: {max}")

# quantile
q0 = num_friends_list[0] #min
print(f"q0: {q0}")

q100 = num_friends_list[len(num_friends_list)-1] #max
print(f"q100: {q100}")

q25 = num_friends_list[int(len(num_friends_list) * 0.25)]
print(f"q25: {q25}")

q50 = num_friends_list[int(len(num_friends_list) * 0.5)] # median
print(f"q50: {q50}")

# numpy
import numpy as np

num_friends_np = np.array(num_friends_list)
max1 = num_friends_np.max()
min1 = num_friends_np.min()
mean = num_friends_np.mean()
median = np.median(num_friends_np)
q0 = np.quantile(num_friends_np, 0)

# 산포도 (dispersion)
# max - min
maxmin = num_friends_np.max() - num_friends_np.min()
print(f"maxmin: {maxmin}")

var = sum((x - mean) ** 2 for x in num_friends_np) / len(num_friends_np)
var_np = np.var(num_friends_np)

print(f"var: {var}") # 분산
print(f"stddev: {var**0.5}") #표준편차

# interquartile range
q75 = np.quantile(num_friends_np, 0.75)
q25 = np.quantile(num_friends_np, 0.25)
print(f"iqr: {q75-q25}")

# histogram
cnt = Counter([x // 10 * 10 for x in num_friends_list]) # 1~9, 10~19까지의 수들을 묶어서 세기 위해 같은 범위에 있는 값을 모두 같은 값을 띠게 만듬
print(cnt)

import matplotlib.pyplot as plt

x, y = zip(*cnt.items())
x = [a+5 for a in x]
plt.bar(x, y, width=10, edgecolor="black")
plt.xlabel("# friends")
plt.ylabel("count")
plt.show()



