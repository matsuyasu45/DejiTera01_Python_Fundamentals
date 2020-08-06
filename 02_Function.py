"""
デジタル寺子屋 第1回  Pythonの基礎 - 02 関数   by まつもと
"""

"""
■02-01 組み込み関数
 Pythonに元から組み込まれている関数で、特に他のファイルを読み込んだりしなくとも
 使える機能です。
"""

# 数値計算の関数たち
a = 1
b = 3
c = 2
d = -1
print('[01] abs(-1) = ', abs(d))   # 絶対値
print('[02] max, min of (1, 3, 2) = ', max(a,b,c),min(a,b,c)) # 最大・最小

# 文字列の関数たち
str_a = "遮断器"
str_b = "Breaker"
print('[03] len of 遮断器, Breaker = ', len(str_a), len(str_b)) # 文字列長

# テキストの入出力の関数たち
message = input('何かタイプしてください。： ')
print('[04] 今入力されたのは', message, 'です。')
e = 15000
pi = 3.141592
print(f"[05] 今日の会費は{e:,}です。円周率は{pi:f}です。小数点2桁までなら{pi:.2f}です。")
                        # {変数:フォーマット}とすると表示時のフォーマットを指定できます。
                        # ,=3桁区切り、f=小数、.nf=小数第n位まで

"""
■02-02 オブジェクトに対する操作（メソッド）
 オブジェクト（文字列等）に対して、その型ごとにさまざまな処理が標準的に用意されています。
"""
# 文字列オブジェクトに対するメソッドたち
str_c = "Osaka"
str_d = "UMEDA"
str_e = "じゅげむじゅげむ、ごこうのすりきれ、かいじゃりすいぎょの"
print('[06] upper and lower = ', str_c.upper(), str_d.lower())  # 大文字、小文字変換
print('[07] じの数 = ', str_e.count('じ')) # 文字の個数のカウント
print('[08] げの位置、あの位置 = ', str_e.find('げ'), str_e.find('あ')) # 文字の位置
print('[09] げをがに置換 = ', str_e.replace('げ', 'が')) # 文字の置換

"""
■02-03 豊富な外部モジュールの関数の活用
 Pythonの魅力は、標準で組み込まれている関数以外に、世界の人々が開発したモジュールを
 自由に読み込んで使えることです。外部モジュールを活用することで、スピーディーに開発を
 進めることができます。
 なぜ外部モジュールをわざわざ読み込むかといえば、要らないものを標準でたくさん抱えて
 いると、メモリを多く消費してしまうから。必要なものを必要な時だけ読み込むのがコツ。
 また、外部モジュールを使う前には「素性」をよく知ってから。知らずに使うのはバグの素。
"""

# 数学関数の外部モジュールmathを読込
import math

pi2 = math.pi # mathの中で定義されている円周率の値（定数）
print('[10] ',pi2,'の小数点以下切り捨ては', math.floor(pi2), '、切り上げは', math.ceil(pi2))
deg45 = math.radians(45)  # 45°をラジアンに変換
print('[11] sin45°=',math.sin(deg45), 'cos45°=', math.cos(deg45), \
      'tan45°=', math.tan(deg45))    # 三角関数も利用可能

# 日付・時間の外部モジュールdatetimeを読込
import datetime

today = datetime.date.today()
now = datetime.datetime.today()
month = today.month
day = today.day
hour = now.hour
min = now.minute

print(f'[12] 今日は{today}、ただいま{now}です。')
print(f'[13] 今日は{month}月{day}日 {hour}時{min}分です。')

# 乱数の外部モジュールrandomのうち整数で乱数を発生させる関数randintのみを読込
from random import randint

dice = randint(1, 6)
print('[14] さいころの目は',dice,'です！')

"""
■02-04 自分で関数を作る！
 あるソフトの中で、同じ処理を繰り返し実行する場合は、その処理を自分で関数として
 定義することで、プログラムをシンプルに書くことができます。
"""
def Reiwa(year):  # 関数Reiwaを定義します。:の後はタブで段下げが必要なことに留意。
    gengo_hyouki = '令和' + str(year-2018) + '年'
    return gengo_hyouki

print('[15] 2021年は', Reiwa(2021))
print('[16] 今年は', Reiwa(today.year))


