import matplotlib.pyplot as plt

friends = [ 70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends, minutes)
for f, m, l in zip(friends, minutes, labels):
    plt.annotate(l, xy=(f, m), xytext=(5, -5), textcoords="offset points") #xytext로 레이블 위치 조정 혹은 xy에 +0,5 해도 됨

plt.show()