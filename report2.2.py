
'''問題２
We measure blood pressure 𝑥O [mmHg] of a patient every hour. We assume the following LDS to model a sequence of the measured blood pressure, 𝑥#, 𝑥".
Use your ID to calculate observed values: 𝑥O = 10 ∗ 𝑏O + 20
我々は毎時間患者の血圧を測定する[mmHg]。 我々は、測定された血圧のシーケンスをモデル化するために、以下のLDSを仮定する。
IDを使用して観測値を計算します：𝑥O= 10 *𝑏O+ 20'''

import numpy as np
import math

class BloodPressure:
  def __init__(self, b3, b2, b1, b0):
    self.b0 = b0
    self.b1 = b1
    self.b2 = b2
    self.b3 = b3

#初期値入力 いちいち入力がめんどいので後でinputに戻す
# print('b3, b2, b1, b0 の順番に半角スペースを空けて入力してください')
# b3, b2 , b1, b0 = map(int, input().split())

b3, b2, b1, b0 = 1, 4, 0, 3 #初期値.あとでinputできるように上と取り替える

b = BloodPressure(b3, b2, b1, b0) #インスタンス作成

  # xt_list = [] #Xt = blood pressure
  # def cal_observed_values(self):
  #   for i, x in enumurate(x):
  #     xt_list.append(x)