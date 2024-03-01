import matplotlib.pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
gdp2 = [340.2, 593.3, 1175.9, 2962.5, 6279.6, 15289.7, 16958.3]

plt.figure(dpi=150) # 선명하게

plt.plot(years, gdp, marker="o", linestyle="dashed", color="red")
# marker 종류 여러개 - 사이트 참고
# linestyle - solid =  "-", dashed = "--", dotted = ":" + custom가능
# custom = linestyle(0, (5,1, ~))
plt.plot(years, gdp2, marker="s", linestyle="--", color="blue") # second graph

#축 이름, 그래프 이름
plt.xlabel("Years")
plt.ylabel("GDP")
plt.title("Title")

#save
#plt.savefig("myfigure.png")

plt.show()