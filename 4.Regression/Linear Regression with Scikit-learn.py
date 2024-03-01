from sklearn.linear_model import LinearRegression

x = [[1, 2], [3, 2], [3, 7], [1, 1], [1, 0]]
y = [[4], [8], [23], [1], [-2]]

lr = LinearRegression() # 모델 생성
lr.fit(x, y) # 입력 데이터, 출력 데이터 - 학습

print(lr.coef_, lr.intercept_) # coef = w, intercept = b
print(lr.predict([[5, 10]])) # 예측 값 - y