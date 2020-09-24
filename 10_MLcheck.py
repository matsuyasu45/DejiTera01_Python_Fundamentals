"""
デジタル寺子屋 第3回  機械学習にトライ - 01 必要なライブラリの準備・確認

　Pythonを使ったデータ分析による機械学習の基礎を学びます。
 機械学習の定番ライブラリ pandas, numpy, sklearnを使いますので、まずこれらを準備
 しましょう。

 1) Pycharmの最下段にある「Terminal」ボタンを押してください。
 2) コマンドプロンプト（>の横）で「pip install pandas」とタイプして、改行してください。
    インストールが進んでいる様子がずらっと表示されるか、「already satisfied」（インス
    トール済）が表示されればOKです。
    ※Macでうまく場合は「pip3 install pandas」と「3」を添えてください。
 3) 同様に、以下の3つのパッケージをインストール（または更新）してください。
    ・ pip install numpy
    ・ pip install sklearn
    ・ pip install matplotlib
 4) このPyhonコードをPycharmで呼び出し、実行してください。
    実行の際には、Pycharmの画面右上の実行ボタン横にある「Edit Configuration」で
    「+」ボタンを押し、「Python File」を選択し、「10_MLcheck.py」を実行することを指定
    してください。（第1回、第2回で習ったとおりです。）
 5) 4つのライブラリのバージョン番号が表示されればOKです。
"""

import pandas as pd
import numpy as np
import matplotlib as mp
import sklearn as sk

print("pandasのバージョン", pd.__version__)
print("numpyのバージョン", np.__version__)
print("matplotlibのバージョン", mp.__version__)
print("scikit-learn(sklearn)のバージョン", sk.__version__)
