import requests
import json

# APIキーの指定
api_key = "d292f60be55545b77c38ca6b7dcc68d3"

# 天気を調べたい都市
cities = ["Tokyo,JP", "London,UK", "New York,US"]
api = "https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

# 温度変換（ケルビン温度→摂氏）
k_to_c = lambda k: k - 273.15

# 温度を取得
for name in cities:
    url = api.format(city=name, key=api_key, lang="ja")
    r = requests.get(url)
    data = json.loads(r.text)

    print("都市 =", data["name"])
    print("| 天気 =", data["weather"][0]["description"])
    print("| 最低気温 =", k_to_c(data["main"]["temp_min"]))
    print("| 最高気温 =", k_to_c(data["main"]["temp_max"]))
    print("| 湿度 =", data["main"]["humidity"])
    print("| 気圧 =", data["main"]["pressure"])
    print("| 風速度 =", data["wind"]["speed"])
    print("--------------------------------")