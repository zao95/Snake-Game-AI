import numpy as np


class Genome:
    def __init__(self):
        self.fitness = 0

        hidden_layer = 10
        # 가우시안 표준정규분포 난수 생성
        self.w1 = np.random.randn(6, hidden_layer)
        self.w2 = np.random.randn(hidden_layer, 20)
        self.w3 = np.random.randn(20, hidden_layer)
        self.w4 = np.random.randn(hidden_layer, 3)

    # 유전자값 별 곱산 후 outfut 출력
    def forward(self, inputs):
        net = np.matmul(inputs, self.w1)
        net = self.relu(net)
        net = np.matmul(net, self.w2)
        net = self.relu(net)
        net = np.matmul(net, self.w3)
        net = self.relu(net)
        net = np.matmul(net, self.w4)
        net = self.softmax(net)
        return net

    # 음수를 0으로 출력하는 정류 선형 유닛
    def relu(self, x):
        return x * (x >= 0)

    # 총합을 0~1로 정규화하는 활성화함수
    def softmax(self, x):
        return np.exp(x) / np.sum(np.exp(x), axis=0)

    # def leaky_relu(self, x):
    #     return np.where(x > 0, x, x * 0.01)

# genome.w1 example
# [[-0.66765064  1.17661647  0.25729579  1.27506605 -2.10919232 -0.08105421
#   -1.04873338 -0.48533909  1.86113836  0.53168706]
#  [-0.81998219 -1.23822589 -0.48544622 -2.31170016 -0.01765465 -1.04863768
#    2.71805947  0.16328487 -1.34934928 -0.85503337]
#  [ 1.9950431   0.17830201 -1.50912914 -0.72741622 -1.01303701 -1.55238029
#   -0.49241003  0.15969216 -0.19807975  0.67812325]
#  [-1.62068139 -0.09019802  0.13038746  0.07479699  0.39352931 -1.30181721
#    2.27745079  0.02541516  0.17029602 -0.05454036]
#  [ 0.20711591  2.09671047 -0.84544548 -0.15783983 -0.63689637  0.09573184
#    1.97788753 -1.20420203  0.1968664  -0.01655162]
#  [ 1.12260396  0.2434821  -2.50321885  0.36800449  1.11468259 -2.06897124
#   -1.29614168 -1.45663835 -0.42499042  0.6736085 ]]