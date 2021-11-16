import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random

nums1 = []

mu1 = 0
sigma1 = 5
mu2 = 5
sigma2 = 5
p = 0.5

for i in range(100000):                                             #生成100000个随机数
    tmp1 = random.gauss(mu1, sigma1)                                #随机数服从 X 的分布
    tmp2 = random.gauss(mu2, sigma2) * np.random.binomial(1, p)     #随机数服从 Y 的分布  η=random.binomial(1, p)
    nums1.append(tmp1 + tmp2)                                       #生成随机数 Z

plt.hist(nums1, bins = 100, color = "#F8BBD0")
#plt.hist(nums2, bins = 200, color = "#4CAF50")
plt.show()