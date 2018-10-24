
'''問題２
We measure blood pressure 𝑥O [mmHg] of a patient every hour. We assume the following LDS to model a sequence of the measured blood pressure, 𝑥#, 𝑥".
Use your ID to calculate observed values: 𝑥O = 10 ∗ 𝑏O + 20
我々は毎時間患者の血圧を測定する[mmHg]。 我々は、測定された血圧のシーケンスをモデル化するために、以下のLDSを仮定する。
IDを使用して観測値を計算します：𝑥O= 10 *𝑏O+ 20'''
  xt_list = [] #Xt = blood pressure
  def cal_observed_values(self):
    for i, x in enumurate(x):
      xt_list.append(x)