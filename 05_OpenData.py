"""
デジタル寺子屋 第1回  Pythonの基礎 - 05 おまけ・オープンデータの描画   by まつもと
  厚生労働省がオープンデータとして公開しているコロナウィルスに関するデータ（CSVファイル）
  を読み込んで、グラフを描いてみましょう。
  　　（参照サイト）https://www.mhlw.go.jp/stf/covid-19/open-data.html
  少し難しい部分があるかもしれませんが、30行足らずのコードでCSVファイルを読んで、グラフ
  を描画して、その画像をファイルに保存できることを「体感」してもらえればと思います。
"""

import csv  # csvファイルの読込用パッケージのインポート
import datetime     # 日付の文字列を日付型の値に変換するためにインポート
import matplotlib.pyplot as pypl  # パッケージの名前が長いのでpyplと略します。

date_str = "2017/11/06"
date_formatted = datetime.datetime.strptime(date_str, "%Y/%m/%d")
print(date_formatted) # 2017-11-06 00:00:00

pcr_file = open("./pcrdata.csv", mode="r", encoding="utf_8")
                    # ファイルを読取モード（r）で開く。文字コードはUTF-8として読込み。
                    # 文字コードを指定しないと文字化けすることがあるので、常に指定を。
                    # 開いたファイルはpcr_fileという変数でアクセスできる。
daily_list = csv.reader(pcr_file, delimiter=",")
                    # ,切り（delimiter=区切り文字）のCSVファイルの内容をdaily_list
                    # という変数に入れる。

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
canvas.savefig('pcr.png')           # canvasに描かれたグラフをpcr.pngに保存

pcr_file.close()    # ファイルを閉じる。これをやらないとファイルが破損する場合もあり。