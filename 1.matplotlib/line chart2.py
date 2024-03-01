import matplotlib.pyplot as plt

variance = [1,2,4,8,16,32,64,128,256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = range(len(variance))
print(xs)

plt.plot(xs, variance, color="r", linestyle="--", marker="s")
plt.plot(xs, bias_squared, color="b", linestyle=":", marker="p")
plt.plot(xs, total_error, color="g", linestyle="-", marker="^")
# plt.plot(xs, total_error, "g-^") - 간단한 표현 방식
# 원하는 색 만들기 color = (0.5, 0.5, 0.5) -> rg  z b 비율 쓰기 (1,1,1) = white / (0,0,0) = black
#f2f3ab -> f2 = r / f3 = g / ab = b : 16진수로 표현된 수 ==> 242 = r / 243 = g / 171 = b (0~255 사이의 수 들어감)
# color = "#00f" 도 가능

# 축값 설정 / 비어있는 리스트 넣으면 값들 지워짐
plt.xticks([0, 8], ["min", "max"]) # 지정된 위치에 지정된 값 입력
plt.yticks([], [])

plt.show()