import numpy as np
import math

n = 5 # サンプル数
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
    u = sum/n
    return u

  def x_upadate(self, x_list, u):
    updated_x = []
    for x in x_list:
      updated_x.append(x - u)
    return updated_x

  def suff_statistics(self, updated_x, zztn):
    square_sample = []
    latent_va = []
    cross_term = []
    for ux, z in zip(updated_x, zztn):
      square_sample.append(np.dot(ux, ux.T))
      latent_va.append(np.dot(z, z.T))
      cross_term.append(np.dot(ux, z.T))
    return square_sample, latent_va, cross_term

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
x_list = np.array([x1, x2, x3, x4, x5], dtype='float')

#mean vector(平均ベクトル) μ導出
u = b.update_u(x_list)
print('μ:{}'.format(u))

#X'n導出 X'n=アップデート後のX
updated_x = b.x_upadate(x_list, u)
print("X'n{}".format(updated_x))

sigma_z_x = 1/2 #共分散Σ(z|x)を求める。簡単なので手計算
zn = (sigma_z_x * (x_list - u))[:,0]
print('それぞれの平均ベクトル(μn(z|x), つまり[Z]nは{} '.format(zn))

#〈ZZ^t〉nを求める
zztn = sigma_z_x + zn * zn.T
print('それぞれの[ZZ^Tn]は{}'.format(zztn))

square_sample, latent_va, cross_term = b.suff_statistics(updated_x, zztn)
square_sum = np.sum(square_sample)
latent_va_sum = np.sum(latent_va)
cross_term_sum = np.sum(cross_term)
print("Sum of squared Samples(X'X'^T):{}\nSum of expectations of squared latent variables(ZZ^T):{}\nSum of cross terms(x'Z^T):{}".format(square_sum, latent_va_sum, cross_term_sum))

# ML estimate of loading matrix　負荷行列 -1<x<1
ml_estimate_loading_matrix = cross_term_sum * (1/latent_va_sum)
print('ML estimate of loading matrix(負荷行列):{}'.format(ml_estimate_loading_matrix)) 

# ML estimate of covariance matrix ç ML estimate= maximum likelihood estimataion
ml_estimate_covariance_matrix = 1/n * np.array((square_sum - cross_term_sum) * ml_estimate_loading_matrix.T)
print('ML estimate of covariance matrix 共分散行列の最尤推定:{}'.format(ml_estimate_covariance_matrix))


#Σ=Covariance matrix 分散共分散行列 参考= https://ja.wikipedia.org/wiki/%E5%88%86%E6%95%A3%E5%85%B1%E5%88%86%E6%95%A3%E8%A1%8C%E5%88%97




