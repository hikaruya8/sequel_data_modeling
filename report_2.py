import numpy as np
import math

class FactorAnalysis:
  def __init__(self, b3, b2, b1, b0):
    self.b0 = b0
    self.b1 = b1
    self.b2 = b2
    self.b3 = b3

  def calc_x(self):
    x1 = (self.b2, self.b3)
    x2 = (self.b1 + self.b3, self.b0 + self.b2)
    x3 = (self.b0 + self.b3, self.b1)
    x4 = (self.b0 + self.b2, self.b1 + self.b2)
    x5 = (self.b0 + self.b2, self.b0 + self.b1 + self.b2)
    return x1, x2, x3, x4, x5

  def update_u(self, x_list):
    sum = 0
    for i in x_list:
      sum += i
    u = sum/5
    return u

  def x_upadate(self, x_list, u):
    updated_x = []
    for x in x_list:
      updated_x.append(x - u)
    return updated_x

#初期値入力 いちいち入力がめんどいので後でinputに戻す
# print('b3, b2, b1, b0 の順番に半角スペースを空けて入力してください')
# b3, b2 , b1, b0 = map(int, input().split())

b3, b2, b1, b0 = 1, 4, 0, 3 #初期値.あとでinputできるように上と取り替える

b = FactorAnalysis(b3, b2, b1, b0) #インスタンス作成

#D次元の確率変数Xn導出, X1=1次元??
#D=Nこの観測点(データ集合）
x1, x2, x3, x4, x5 = b.calc_x()
print('x1:{} , x2:{} ,x3:{} ,x4:{} , x5:{}'.format(x1, x2, x3, x4, x5))

#Xnリスト化(numpy)
x_list = np.array([x1, x2, x3, x4, x5])

#mean vector(平均ベクトル) μ導出
u = b.update_u(x_list)
print('μ:{}'.format(u))

#X'n導出 X'n=アップデート後のX
updated_x = b.x_upadate(x_list, u)
print("X'n{}".format(updated_x))

# #モデルの潜在変数zの導出 z=μの単位ベクトル
# norm_u = np.linalg.norm(u)
# z = u/norm_u
# print('潜在変数 (factor_z) {}'.format(z))

#Σ=Covariance matrix 分散共分散行列 参考= https://ja.wikipedia.org/wiki/%E5%88%86%E6%95%A3%E5%85%B1%E5%88%86%E6%95%A3%E8%A1%8C%E5%88%97




