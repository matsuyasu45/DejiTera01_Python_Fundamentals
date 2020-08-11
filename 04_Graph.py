"""
デジタル寺子屋 第1回  Pythonの基礎 - 04 グラフ描画   by まつもと

基礎の基礎ばかりだとつまらないので、第1回の締めとして「グラフの描画」にトライします。
グラフの元となるデータを格納する型として「リスト」が出てきますが、詳しくは第2回でレクチャーします。
ここでは、[]の中に,切りでデータが並んでいるのが「リスト」だ理解しておけばＯＫです。
"""

"""
■04-01 グラフ描画用パッケージの読込
  ※グラフ内に日本語を書くと文字化けしてしまう問題は、フォントのダウンロードで解決でき
    ます。「matplotlib 文字化け 日本語 Windows/Mac」で検索してみてください。
    寺子屋の中では解決処置を割愛します。
"""
import matplotlib.pyplot as pypl  # パッケージの名前が長いのでpyplと略します。

"""
■04-02 折れ線グラフ1
"""
oresen_data = [ 100, 300, 400, 450, 200 ] # Y軸の値（X軸はデフォルトで1刻み）
pypl.plot(oresen_data)
pypl.show()

"""
■04-02 折れ線グラフ2
"""
oresen_x_data = [ 4, 10, 15,  20, 25 ]          # X軸の値
oresen_y1_data = [ 100, 300, 400, 450, 700 ]     # 系列1のY軸の値
oresen_y2_data = [ 200, 100, 50, 150 , 300 ]     # 系列2のY軸の値
pypl.plot(oresen_x_data, oresen_y1_data, color="blue", marker="*")
pypl.plot(oresen_x_data, oresen_y2_data, color="red", marker="X")
                                # マーカーの文字は決まったもののみ使える。
pypl.title("Trend of Damage")   # グラフのタイトル
pypl.xlabel("Year")       # X軸のタイトル
pypl.ylabel("Faults")           # Y軸のタイトル
pypl.grid(True)                 # グラフ上の格子
pypl.show()

"""
■04-03 棒グラフ
"""
fuken = ['Osaka', 'Hyogo', 'Kyoto', 'Nara', 'Shiga', 'Wakayama']
narabi = range(5,-1,-1)     # 5から1ずつ減じて-1より上まで。つまり[5,4,3,2,1,0]のこと。
kansen = [102, 30, 10, 4, 3, 2]
pypl.barh(narabi, kansen, tick_label = fuken)
pypl.title("COVID-19 Kansen-sha-su in Kinki on 11th Aug. 2020")   # グラフのタイトル
pypl.show()

"""
■04-04 積上げ棒グラフ
"""
fuken = ['Osaka', 'Hyogo', 'Kyoto', 'Nara', 'Shiga', 'Wakayama']
narabi = range(0,6,1)     # 0から1ずつ増やして6より下まで。つまり[0,1,2,3,4,5]のこと。
kansen09 = [195, 48, 20, 12, 8, 5]
kansen10 = [123, 26, 8, 6, 7, 3]
bar09 = pypl.bar(narabi, kansen09, color="purple")
bar10 = pypl.bar(narabi, kansen10, color="orange", bottom=kansen09)
pypl.xticks(narabi, fuken)
pypl.title("COVID-19 Kansen-sha-su in Kinki on 9th-10th Aug. 2020")   # グラフのタイトル
pypl.legend((bar09, bar10), ("9th", "10th"))
pypl.show()
#値が3つ以上の場合はbottomの値を指定するためにリストの足し算をする必要があります。
#そのため、numpyというパッケージをimportし、arrayという関数を使う必要があるのですが、
#今回は省略します。興味があれば検索してみてください。

"""
■04-05 散分図
"""
kion = [ 10.5, 14.3, 17.8, 20.1, 26.9, 23.2, 29.8, 34.5]
denryu = [ 1.82, 1.74, 1.67, 1.55, 1.38, 1.46, 1.29, 1.16]
pypl.scatter(kion, denryu)
pypl.show()

"""
matplotlibでは、他にも円グラフ、バブルチャート、ヒストグラム、チャートなど多彩なグラフを
描くことができます。興味があれば「matplotlib グラフ 種類」で検索してみてください。
"""

