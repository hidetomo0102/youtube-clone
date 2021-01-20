from sklearn import svm, metrics
import glob, os.path, re, json


# テキストを読んで出現頻度を調べる
def check_frequency(file_name):
    name = os.path.basename(file_name)
    lang = re.match(r'^[a-z]{2,}', name).group()
    with open(file_name, "r", encoding="utf-8") as f:
        text = f.read()
    text = text.lower()
    # カウンタを0に
    count = [0 for n in range(0, 26)]
    code_a = ord("a")
    code_z = ord("z")
    # アルファベットの出現回数を調べる
    for ch in text:
        n = ord(ch)
        if code_a <= n <= code_z:
            count[n - code_a] += 1
    # 正規化する
    total = sum(count)
    frequency = list(map(lambda n: n / total, count))
    return frequency, lang


# 各ファイルを処理する
def load_files(path):
    freqs = []
    labels = []
    file_list = glob.glob(path)
    for file_name in file_list:
        r = check_frequency(file_name)
        freqs.append(r[0])
        labels.append(r[1])
    return {"freqs": freqs, "labels": labels}


data = load_files("./lang/train/*.txt")
test = load_files("./lang/test/*.txt")
# JSONで結果を保存
with open("./lang/freq.json", "w", encoding="utf-8") as fp:
    json.dump([data, test], fp)

# 学習
clf = svm.SVC()
clf.fit(data["freqs"], data["labels"])

# 予測
predict = clf.predict(test["freqs"])

# 結果の確認
accuracy_score = metrics.accuracy_score(test["labels"], predict)
cl_report = metrics.classification_report(test["labels"], predict)
print("正解率=", accuracy_score)
print("レポート=")
print(cl_report)