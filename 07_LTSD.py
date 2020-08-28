"""
デジタル寺子屋 第2回  Pythonの基礎 - 07 リスト

 ビッグデータ解析等、応用プログラムに必要不可欠なさまざまなデータ構造として、以下の4つの
 うちリストを紹介します。
   * リスト ： 値の並びです。リストを作成後に変更（追加、削除）もできます。
   ・ タプル ： 複数の値の組を1つの値として扱うためのものです。作成後の変更はできません。
   ・ 集合（セット） ： かつて数学で習った？集合そのものです。
   ・ 辞書（ディクショナリ） ： キーを与えると値が返ってきます。単語で引くと意味が返ってくる
     「国語辞典」を思い出してみてください。
"""

"""
■07-01 リスト
 値の並びです。リストを作成後に変更（追加、削除）もできます。
"""

# リストの基本
shikoku = ["Kagawa", "Tokushima", "Ehime", "Kochi"]
print("[01] shikoku[1]=", shikoku[1], " shikoku[-1]=", shikoku[-1])
    # リストの1番目の要素は[0]で参照、その後は[1]、[2]。後からの参照は[-1]、[-2]で。
print("[02] shikokuの要素数=", len(shikoku))

sushi = ["Maguro", "Uni", "Hamachi"]
print("[03] sushi=", sushi)
sushi.append("Ebi")         # リストの末尾にEbiを追加
print("[04] sushi=", sushi)
sushi.insert(2, "Tai")      # リストの指定位置（2）にTaiを追加
print("[05] sushi=", sushi)


# リストの要素の操作
animal1 = ["0_rabbit", "1_mouse", "2_dog"]
animal2 = ["3_elephant", "4_tiger", "5_bear"]
animals = animal1 + animal2     # リストを連結
print("[06] animal1=", animal1, "\n     animal2=", animal2, "\n     animals=", animals)
print("[07] animals[1:4]=", animals[1:4])     # 1から4の手間(=3)まで
print("[08] animals[2:]=", animals[2:])      # 2より後
print("[09] animals[:-2]=", animals[:-2])     # 後から2番目の手前まで
print("[10] animals[0:6:2]=", animals[0:6:2])   # 先頭（0）から6番目の手前（=5）まで2つ刻みで

# リスト同士の比較
fruits1 = ["apple", "orange", "peach"]
fruits2 = ["apple", "orange", "peach"]
fruits3 = ["orange", "apple", "peach"]
print("[11] fruits1==fruits2:", fruits1==fruits2,
        "/ fruits1==fruits3:", fruits1==fruits3)    # 中身は同じでも順序が違えば別物

# リストのコピー
fruits4 = fruits1       # 参照渡し。fruits1のメモリ領域の先頭アドレスをfruits4にコピー
fruits1.append("lemon")
print("[12] fruits1=", fruits1, "/ fruits4=", fruits4)
fruits5 = fruits2.copy()    # 値渡し。fruits2の内容を別のメモリ領域fruits5に丸々コピー
fruits2.append("lemon")
print("[13] fruits2=", fruits2, "/ fruits5=", fruits5)

# リスト要素の並べ替え
nums = [50, 80, 40, 100, 10]
print("[14] nums=", nums)
nums.sort()     # 昇順に並べ替え
print("[15] nums=", nums)

fruits6 = ["melon", "apple", "orange", "banana", "peach"]
print("[16] fruits6=", fruits6)
fruits6.sort()     # 昇順に並べ替え
print("[17] fruits6.sort=", fruits6)

fruits7 = ["melon", "apple", "orange"]
fruits8 = sorted(fruits7)
print("[18] fruits7=", fruits7)
print("[19] sorted(fruits7)=", fruits8)

# 要素の順次取り出し・削除・各種検索
sushi = ["Otoro", "Tamago", "Kanpachi", "Unagi", "Saba", "Kanpachi"]
for neta in sushi:          # リストに含まれるアイテムを一つずつnetaに入れて処理
    print("[20] neta = ", neta)
for neta in sushi:
    if neta=="Tamago":      # Tamagoが入ってたらリストから削除する。
        sushi.remove(neta)
print("[21] sushi=", sushi)
if "Kanpachi" in sushi:     # Kanpachiがsushiの中に入っていれば実行
    print("[22] カンパチ", sushi.count("Kanpachi"), "カン、お待ち！")   # 個数をcount
print("[23] サバは", sushi.index("Saba")+1,"番目です。") #indexで先頭から何番目かを調査

# コンマ切り、スペース切りの文字列をリストにセット
csv_string = "100,500,200,300,600"   # CSVファイルのとある1行を
csv_items = csv_string.split(",")   # ,記号で区切ってリストcsv_itemsに入れてみる。
print("[24] csvファイルから作ったリスト=",csv_items)
for yen in csv_items:
    print("[25] お会計は", yen, "円です。")

# リスト要素の最大・最小・合計
scores = [80, 76, 90, 102, 96, 153, 128]
print("[26] max=", max(scores), "/ min=", min(scores), "/ sum=", sum(scores))