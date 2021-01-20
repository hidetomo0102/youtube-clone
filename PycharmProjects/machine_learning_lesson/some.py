from sklearn import svm, metrics
import random, re


# アヤメのCSVデータを読み込む
lines = open('iris.csv', "r", encoding="utf-8").read().split("\n")
f_tonum = lambda n : float(n) if re.match(r'^[0-9.]+$', n) else n
f_cols = lambda i : list(map(f_tonum, i.split().split(",")))
csv = list(map(f_cols, lines))
del csv[0]
random.shuffle(csv)