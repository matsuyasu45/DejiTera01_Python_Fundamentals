"""
デジタル寺子屋 第2回  Pythonの基礎 - 08 タプル・集合（セット）・辞書（ディクショナリ）

 ビッグデータ解析等、応用プログラムに必要不可欠なさまざまなデータ構造として、以下の*の3つを
 紹介します。
   ・ リスト ： 値の並びです。リストを作成後に変更（追加、削除）もできます。
   * タプル ： 複数の値の組を1つの値として扱うためのものです。作成後の変更はできません。
   * 集合（セット） ： かつて数学で習った？集合そのものです。
   * 辞書（ディクショナリ） ： キーを与えると値が返ってきます。単語で引くと意味が返ってくる
     「国語辞典」を思い出してみてください。
"""

"""
■08-01 タプル
 複数の値の「組」を１つの値として扱います。作成後の変更不可（イミュータブル）です。
"""
tuple_a = (1, 2)
tuple_b = (3, "Python")
tuple_c = tuple(range(-3, 6, 2))
tuple_d = tuple("水金地火木土天海冥")
print("[01] タプルたち：", tuple_a, tuple_b, tuple_c, tuple_d)
print("[02] タプルからの抜取りa：", tuple_a[0], tuple_a[1])
print("[03] タプルからの抜取りd：", tuple_d[1:3], tuple_d[2:7:2], tuple_d[2::2])

# タプルの内容を複数の変数に取り分け（アンパックし）ます。
num, gengo = tuple_b
print("[04] num=", num, "/ gengo=", gengo)

# タプルの内容を順番に取り出して処理します。
for wakusei in tuple_d:
    print("[05]", wakusei, end="/ ") # printの「end」で末尾の文字を指定できます。
print("\n・・・惑星リスト、以上です。")     # 文字列に\nを入れると改行を示します。
for i, wakusei in enumerate(tuple_d):   # enumerateで囲うとループの序列も取り出せます。
    print("[06] ", "太陽系第", i+1, "惑星は「", wakusei, "」で始まるあの惑星です。", sep="")
                                        # printの「sep」で,部の文字を指定できます。

# タプルの比較
tuple_e = (1, 2)
tuple_f = (2, 1)
print(f"[07] a={tuple_a}, e={tuple_e}, f={tuple_f}") # printでfで始めて{}で変数を表示可。
print("[08] aとe、eとfのタプルは同じでしょうか？", tuple_a==tuple_e, tuple_e==tuple_f)

"""
■08-02 集合（セット）
 かつて数学で習った？集合そのものです。
"""
midosuji_stations = {"中津", "梅田", "淀屋橋", "本町", "心斎橋", "なんば"}
yotsubashi_stations = {"西梅田", "肥後橋", "本町", "心斎橋", "なんば"}
kara_stations = set()   # 空の集合はset()で作れます。

print("[09] 御堂筋線の駅の集合の要素数は", len(midosuji_stations))
print("[10] 四つ橋線の駅の集合は", yotsubashi_stations)
yotsubashi_stations.add("住之江公園")        # 集合に要素を追加
print("[11] 四つ橋線の駅の集合は", yotsubashi_stations)
yotsubashi_stations.discard("住之江公園")    # 集合から要素を削除
print("[12] 四つ橋線の駅の集合は", yotsubashi_stations)

kyotsu_stations = midosuji_stations & yotsubashi_stations   # 積集合
all_stations = midosuji_stations | yotsubashi_stations      # 和集合
sabun_stations = midosuji_stations - yotsubashi_stations    # 差集合
print("[13] 御堂筋線と四つ橋線で共通の駅は", kyotsu_stations)
print("[14] 御堂筋線と四つ橋線の駅は", all_stations)
print("[15] 御堂筋線だけにある駅は", sabun_stations)

nozomi_stations = {"新大阪", "京都", "名古屋"}
kodama_stations = {"新大阪", "京都", "米原", "岐阜羽島", "名古屋"}
hayate_stations = {"東京", "上野", "大宮", "仙台", "盛岡"}
mizuho_stations = {"新大阪", "新神戸", "岡山", "広島", "小倉", "博多", "熊本"}

print("[16] のぞみ停車駅とこだま停車駅は同じ？違う？",
      nozomi_stations==kodama_stations, nozomi_stations!=kodama_stations)
print("[17] のぞみ停車駅とはやて停車駅に共通の駅はありせんか？",
      nozomi_stations.isdisjoint(hayate_stations))  # disjoint＝互いに素
print("[18] では、のぞみ停車駅とみずほ停車駅に共通の駅はありせんか？",
      nozomi_stations.isdisjoint(mizuho_stations))
print("[19] のぞみ停車駅はこだま停車駅に完全に含まれますか？",
      nozomi_stations.issubset(kodama_stations))    # subset=部分集合
print("[20] こだま停車駅はのぞみ停車駅を完全に含みますか？",
      nozomi_stations.issuperset(kodama_stations))  # subset=上位集合

"""
■08-03 辞書
 1冊の辞書 = { 単語1: 意味1, 単語2: 意味2, ・・・ ｝ のように定義します。
 辞書ですので、追加・変更・削除が可能です。また、さまざまな形で辞書を「引く」ことができます。
"""
# 御堂筋線の駅ナンバリングと駅名の辞書（文字列：文字列）
Midosuji_num = {"M16": "梅田", "M17": "淀屋橋", "M18": "本町",
                "M19": "心斎橋", "M20": "なんば"}
print("[21] 御堂筋線M16の駅は", Midosuji_num["M16"], "駅です。", sep="")
                        # print文でsep="@@@"とすると、,の間の文字列が@@@になります。

# 御堂筋線の駅ナンバリング（M抜き）と駅名の辞書（数値：文字列）
Midosuji_Mnum = { 16: "梅田", 17: "淀屋橋", 18: "本町", 19: "心斎橋", 20: "なんば"}
print("[22] 御堂筋線M17の駅は", Midosuji_Mnum[17], "駅です。")

# 新大阪駅から御堂筋線各駅までの大人普通運賃の辞書（文字列:数値）
Midosuji_fare_from_ShinOsaka = { "梅田": 230, "淀屋橋": 230, "本町": 230,
                                 "心斎橋": 230, "なんば": 280}
print("[23] 新大阪駅から本町駅までの大人普通運賃は", \
      Midosuji_fare_from_ShinOsaka["本町"], "円です。")

# 御堂筋線の駅名のひらがなとローマ字表記の辞書（文字列:タプル）
Midosuji_tagengo = { "梅田": ("うめだ", "Umeda", "梅田", "우메다"),
                     "淀屋橋": ("よどやばし", "Yodoyabashi", "淀屋桥", "요도야바시"),
                     "本町": ("ほんまち", "Hommachi", "혼마치"),
                     "心斎橋": ("しんさいばし", "Shinsaibashi", "心斋桥", "신사이바시"),
                      "なんば": ("なんば", "Namba", "难波", "난바")}
print("[24] つぎは", Midosuji_tagengo["心斎橋"][0], "です。")
print("[25] The next station is", Midosuji_tagengo["なんば"][1], ".")
print("[26] 下一站", Midosuji_tagengo["心斎橋"][2], ".")   # xīn心zhāi斋qiáo桥
print("[27] 이번역은", Midosuji_tagengo["淀屋橋"][3], "입니다.")

# 辞書への値の追加・更新・追加・削除
print("[28] Midosuji_numの元の辞書＝", Midosuji_num)
Midosuji_num["M15"] = "中津" # 辞書への新たなキーの追加
print("[29] Midosuji_numの中津追加後の辞書＝", Midosuji_num)
Midosuji_num["M16"] = "大阪梅田（おっと・・・？！）"  # 辞書のあるキーの値の変更
print("[30] Midosuji_numの梅田変更後の辞書＝", Midosuji_num)
del Midosuji_num["M20"]     # 辞書のあるキーの削除
print("[31] Midosuji_numのなんば削除後の辞書＝", Midosuji_num)
Midosuji_num.clear()        # 辞書の完全な削除
print("[32] Midosuji_numの完全削除後の辞書＝", Midosuji_num)

# 空の辞書からスタートする。
karano_jisho = dict()       # dict()で空の辞書を作成
print("[33] 空の辞書＝", karano_jisho)
karano_jisho["空やのに"] = "空ちゃうやん"
print("[34] 空の辞書＝", karano_jisho)

# すべての値を取り出してみる。
for ekimei in Midosuji_fare_from_ShinOsaka:  # キーの値を順にekimeiにセット
    fare = Midosuji_fare_from_ShinOsaka[ekimei]
    print("[35] 新大阪駅から", ekimei, "駅までの大人普通運賃は", fare, "円です。")

# 辞書のコピー、2つの方法
dict_a = {7: "July", 8: "August"}
dict_b = {7: "July", 8: "August"}
dict_c = dict_a         # 辞書aの格納メモリ領域の「頭位置」をコピーしています。（参照渡し）
dict_c[8] = "葉月"
print(f"[36] 集合aは{dict_a}、集合cの値は{dict_c}で、同一性は{dict_a==dict_c}です。")
dict_d = dict_b.copy()  # 辞書bの内容一式をコピーしています。（値渡し）
dict_d[8] = "葉月"
print(f"[36] 集合bは{dict_b}、集合cの値は{dict_d}で、同一性は{dict_b==dict_d}です。")

# 強制終了する命令を入れてあるので、次の応用編を実行する場合は次の行の先頭に#でコメントアウト
exit()

# 最後に、ちょっと応用編を。
# 7月と8月の英語だけ知ってる辞書に教えを乞う場合のPythonプログラムの例です。
dict_e = {7: "July", 8: "August"}   # 辞書に7月と8月の英語を教える。
while True:     # break命令が実行されるまで無限ループ（＝常時True)で実行
    month_num = input("[37] 何月のことを調べますか？（終了時は0）： ")
    if not month_num.isdigit():     # month_numが数値（digit）でなければ・・・
        print(f"[38] これこれ、数値以外入れるでない。もう一度。")
        continue                    # もう一度上のwhileに戻ってやり直し
    else:
        month_num = int(month_num)  # 数値であれば、month_numは文字列なので数値に変換

    if month_num==0:
        break   # 0が入力されたら終了
    else:       # 0以外の数値なら以下を実行
        try:    # エラー覚悟で次の処理をやってみる。うまくいけばそのままスルー。
            month_english = dict_e[month_num]
            print(f"[39] {month_num}月の英語は{month_english}じゃ。")
        except KeyError:    # KeyErrorというエラーが発生したら・・・
            print(f"[40] {month_num}は世の辞書にはないのじゃ。")
        except Exception as error:  # その他のエラー（Exception）が発生したら・・・
            print(f"[41] 知らんけど、{error}のエラーじゃ。")