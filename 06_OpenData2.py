"""
デジタル寺子屋 第1回  Pythonの基礎 - 06 おまけ2・オープンデータの描画   by まつもと
  厚生労働省がオープンデータとして公開しているコロナウィルスに関するデータ（CSVファイル）
  を【ネット経由で】読み込んで、グラフを描いてみましょう。
  　　（参照サイト）https://www.mhlw.go.jp/content/pcr_positive_daily.csv
  05の「おまけ」で★の部分を変更したものです。
"""

import csv  # csvファイルの読込用パッケージのインポート
import datetime    # 日付の文字列を日付型の値に変換するためにインポート
import matplotlib.pyplot as pypl  # パッケージの名前が長いのでpyplと略します。
import urllib.request  # ★URLを指定してファイルをダウンロードするためのパッケージ

# ★インターネット上で公開されているCSVファイルをdll_dataに保存
url = "https://www.mhlw.go.jp/content/pcr_positive_daily.csv"  # 読み込むファイルのURL
urllib.request.urlretrieve(url, "./pcrdata.csv")  # 指定したURLのファイルを指定したローカルパスに名前を

# === ここからは先ほどとまったく同じ！！ ===
pcr_file = open("./pcrdata.csv", mode="r", encoding="utf_8")
daily_list = csv.reader(pcr_file, delimiter=",")

hizuke = []  # 日付のリストを初期化（空のリスト）
yousei = []  # 陽性者数のリストを初期化（空のリスト）
header = next(daily_list)   # 1行目をheaderという変数に入れて読み捨てる。
for daily_data in daily_list:
    hiduke_value = datetime.datetime.strptime(daily_data[0], '%Y/%m/%d')
    hizuke.append(hiduke_value)
    yousei.append(int(daily_data[1]))

# グラフ描画用リストの作成状況の表示
print('日付（hizuke）のリスト＝', hizuke)    # X軸の変数
print('陽性者（yousei)のリスト＝', yousei)  # Y軸の変数

canvas = pypl.figure()              # グラフ描画エリアをcanvas変数にセット
pypl.plot(hizuke, yousei, color="red", marker="*")
pypl.title("Trend of COVID-19 Positives")   # グラフのタイトル
pypl.xlabel("Date")                 # X軸のタイトル
pypl.ylabel("Number of Positives")  # Y軸のタイトル
pypl.grid(True)                     # グラフ上の格子
pypl.show()
canvas.savefig('pcr_dll.png')           # canvasに描かれたグラフをpcr.pngに保存

pcr_file.close()    # ファイルを閉じる。これをやらないとファイルが破損する場合もあり。