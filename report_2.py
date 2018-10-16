import numpy as np

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

#xn導出
x1, x2, x3, x4, x5 = b.calc_x()
print('x1:{} , x2:{} ,x3:{} ,x4:{} , x5:{}'.format(x1, x2, x3, x4, x5))

#xnリスト化(numpy)
x_list = np.array([x1, x2, x3, x4, x5])

#μ導出
u = b.update_u(x_list)
print('μ:{}'.format(u))

#X'n導出
updated_x = b.x_upadate(x_list, u)
print("X'n{}".format(updated_x))


