class factor_analysis:
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

  def update_u(self):
    u = (u1, u2)


# a,b = map(int,input().split())
print('b3, b2, b1, b0 の順番に半角スペースを空けて入力してください')
b3, b2 , b1, b0 = map(int, input().split())
myinstance = factor_analysis(b3, b2, b1, b0)
x1, x2, x3, x4, x5 = myinstance.calc_x()
print('x1:{} , x2:{} ,x3:{} ,x4:{} , x5:{}'.format(x1, x2, x3, x4, x5))


