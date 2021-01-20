import pandas as pd
from sklearn import svm, metrics, model_selection
import random, re

# アヤメのCSVデータを読み込む
csv = pd.read_csv("iris.csv")

# リストを訓練データとラベルに分割する
data = csv[["sepal.length", "sepal.width", "petal.length", "petal.width"]]
label = csv["variety"]

# クロスバリエーション
clf = svm.SVC()
score = model_selection.cross_val_score(clf, data, label, cv=5)
print("各正解率=", score)
print("正解率=", score.mean())