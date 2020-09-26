"""
デジタル寺子屋 第3回  機械学習にトライ - 02 ボストンの住宅価格の予測(2) 重回帰分析

　Pythonを使ったデータ分析による機械学習の基礎を学びます。
 Pythonを使った機械学習を学ぶ人のために提供されている「米国ボストン市郊外における
 地域別の住宅価格のデータセット」をCSVファイル化したboston2.csvを題材として使います。
 重回帰とは、複数の説明変数を使って目的変数を精度よく予測しようとする分析手法です。

 ＜boston2.csvの構造＞
   * データの規模： レコード（地域のサンプル）数 506、 カラム数 14
   * 説明変数のデータ項目
    - CRIM： 犯罪発生率
    - ZN： 住居区画の密集度
    - INDUS： 非小売業の土地割合
    - CHAS： チャールズ川の周辺かどうか (1: 川の周辺, 0: それ以外)
    - NOX： 窒素酸化物（NOx）の濃度
    - RM： 平均部屋数
    - AGE： 1940年より前に建てられた物件割合
    - DIS： 5つのボストン市の雇用施設からの重み付き距離
    - RAD： 大きな道路へのアクセスしやすさ
    - TAX： $10,000ドルあたりの所得税率
    - PTRATIO： 教師あたりの生徒数
    - LSTAT： 低所得者の割合
   * 目的変数
    - PRICE： 当該地域の平均住宅価格 （CSVファイルの一番右側）
"""

# 必要なライブラリを読込
import pandas as pd                     # データ分析用ライブラリ
import numpy as np
from matplotlib import pyplot as plt    # グラフの描画用ライブラリ
# 機械学習用ライブラリsklearn（正式名称はscikit-learn（サイキットラーン））から・・・
from sklearn.linear_model import LinearRegression as LR     # 線形回帰ライブラリ
from sklearn.model_selection import train_test_split        # データ分離ライブラリ

# 定数の設定
SETSUMEI = ["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", \
            "RAD", "TAX", "PTRATIO", "LSTAT"]  # 説明変数のラベル
MOKUTEKI = "PRICE"  # 目的変数のラベル

# boston2.csvの読込（boston2.csvのデータ一式を変数original_dataに読込）
#   ※参考： Excelファイルを読み込むためにread_excelという関数もあります。
original_data = pd.read_csv("boston2.csv")
# 全変数相互間の散布図による相関分析（全体像の把握）
#pd.plotting.scatter_matrix(original_data)

# 単回帰分析で使用する説明変数のリストをXに、目的変数のリストをYにセット
X = original_data[SETSUMEI]
y = original_data[MOKUTEKI]

# (X<Y)の組を学習用（訓練用）データtrainと評価用データtestに分離
#   ここでは学習用7:評価用3に振り分けます。
#   ※参考： shuffle=FalseだとCSVファイルの上と下で分離、Trueとするとシャッフルして分離します。
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=True)

# 読み込んだデータの基礎分析
print('[01] ', original_data.shape)     # CSVファイルのデータの行数、列数の確認
print('[02]\n', original_data.head(5))   # CSVファイルの先頭5行の確認
print('[03]\n', X_train.head(5))     # 学習用データの説明変数Xの先頭5行を表示
print('[04]\n', y_train.head(5))     # 学習用データの目的変数Yの先頭5行を表示
                                    # [04],[05]の最左列はCSVファイルの行番号です。
print('[05] 分離前の全データの説明変数Xの基本統計量\n', X.describe())
print('[06] 学習用データの説明変数Xの基本統計量\n', X_train.describe())
print('[07] 評価用データの説明変数Xの基本統計量\n', X_test.describe())
                                    # count=データの個数、 mean=平均値、 std=標準偏差
                                    # min=最小値、50%=中央値、max=最大値

# 欠損データの確認
#   ※もし欠測データがあった場合には、dropna関数で当該行のデータを削除、もしくはfillna
#     関数で仮の値を補充し、誤ったデータをもとに学習してしまわないようにします。
print("[08] 学習用データの欠測値の個数（X,Y）＝\n", X_train.isnull().sum(), y_train.isnull().sum())
print("[09] 評価用データの欠測値の個数（X,Y）＝\n", X_test.isnull().sum(), y_test.isnull().sum())

# 線形回帰による単回帰分析の実行
model = LR()            # 線形回帰のための器をLRライブラリを使って変数modelに準備
model.fit(X_train, y_train) # 学習用データ（X_train, Y_train)を使って線形回帰分析
print(f"[11] 近似式は {MOKUTEKI} = {SETSUMEI} * {model.coef_} + {model.intercept_}")

# 線形回帰分析の結果得られたモデル（model）を評価用データに適用して精度をチェック
print("[12] 得られたモデルの評価用データへの適用時の決定係数R^2（最良=1）は", model.score(X_test,y_test))

# 線形近似ではなく、曲線近似をさせるにはscipyライブラリを使う方法があります。
# ここでは解説しませんが、興味があれば調べてみてください。
