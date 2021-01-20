from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import random, re
import pandas as pd

# アヤメのCSVを読み込む
csv = pd.read_csv("iris.csv")

# 任意の列を取り出す
csv_data = csv[["sepal.length", "sepal.width", "petal.length", "petal.width"]]
csv_label = csv["variety"]

# 学習用とテスト用に分割
train_data, test_data, train_label, test_label = train_test_split(csv_data, csv_label)

# データを学習し、予測する
clf = svm.SVC()
clf.fit(train_data, train_label)
pre = clf.predict(test_data)

# 正解率を見る
accurate_score = metrics.accuracy_score(test_label, pre)
print("正解率=", accurate_score)