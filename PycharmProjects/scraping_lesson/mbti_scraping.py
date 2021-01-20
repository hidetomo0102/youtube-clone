import glob
import os.path
import time

from selenium import webdriver

# URLと選択肢を用意
TARGET_URL = "https://www.16personalities.com/ja/%e6%80%a7%e6%a0%bc%e8%a8%ba%e6%96%ad%e3%83%86%e3%82%b9%e3%83%88"

CHOICE_MAP = {
    3: ".agree.max",
    2: ".agree.med",
    1: ".agree.min",
    0: ".neutral",
    -1: ".disagree.min",
    -2: ".disagree.med",
    -3: ".disagree.max",
}
# ドライバーを指定
DRIVER_MAC = "./chromedriver"

INTERVAL = 3


# ブラウザを起動
driver_path = DRIVER_MAC
driver = webdriver.Chrome(executable_path=driver_path)
driver.maximize_window()
time.sleep(INTERVAL)

# ファイルを取得
file_list = glob.glob("data/*.csv")

for csv_file in file_list:

    # 対象のサイトへアクセス
    driver.get(TARGET_URL)
    time.sleep(INTERVAL)

    # ファイルを開く
    with open(csv_file) as f:
        # １行ずつの配列に変換
        lines = [int(line) for line in f.read().splitlines()]
        # 6つずつループする
        for i in range(0, len(lines), 6):
            # 回答ボタンを取得
            decisions = driver.find_elements_by_css_selector(".decision:not(.mobile)")
            for j in range(i, i+6):
                decisions[j % 6].find_element_by_css_selector(CHOICE_MAP[lines[j]]).click()
            time.sleep(1)
            # 次へボタンを押す
            driver.find_element_by_tag_name("button").click()
            time.sleep(INTERVAL)

    # 結果画面でデータを取得
    type_name = driver.find_element_by_class_name("type-name").text
    type_code = driver.find_element_by_class_name("type-code").text
    type_url = driver.current_url

    # ファイル名から診断者の名前を取得
    file_name = os.path.dirname(csv_file)
    name, ext = os.path.splitext(file_name)
    print(f"{name}さんのMBTIは{type_name}(タイプコード：{type_code})です。\n URL: {type_url}")
    time.sleep(INTERVAL)

# 最後にブラウザを閉じる
driver.quit()