from sklearn import svm, metrics
import random, re

# アヤメのCSVデータを読み込む
lines = open('iris.csv', "r", encoding="utf-8").read().split("\n")
f_tonum = lambda n: float(n) if re.match(r'^[0-9.]+$', n) else n
f_cols = lambda i: list(map(f_tonum, i.strip().split(",")))
csv = list(map(f_cols, lines))
del csv[0]
random.shuffle(csv)

# データをK分割する
K = 5
csv_perK = [[] for i in range(K)]
for i in range(len(csv)):
    csv_perK[i % K].append(csv[i])


# リストを訓練データとラベルに分割する関数
def split_data_label(rows):
    data = []
    label = []
    for row in rows:
        data.append(row[0:4])
        label.append(row[4])
    return data, label


# 正解を求める
def calculate_score(test, train):
    test_f, test_l = split_data_label(test)
    train_f, train_l = split_data_label(train)
    clf = svm.SVC()
    clf.fit(train_f, train_l)
    pre = clf.predict(test_f)
    return metrics.accuracy_score(test_l, pre)


# 分割したKデータについて正解率を求める
score_list = []
for testc in csv_perK:
    trainc = []
    for i in csv_perK:
        if i != testc: trainc += i
    score = calculate_score(testc, trainc)
    score_list.append(score)

print("各正解率=", score_list)
print("平均正解率=", sum(score_list) / len(score_list))