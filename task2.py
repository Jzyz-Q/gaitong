import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random

nums1 = []
u = []
ans = []

mu1 = 3
sigma1 = 50
mu2 = 200
sigma2 = 200
p = 0.3
n = 1000

EZ = mu1 + p*mu2
DZ = sigma1*sigma1 + p*sigma2*sigma2 + p*mu2*mu2 - p*p*mu2*mu2

for i in range(1000):
    ans.append(0)

for i in range(1000): #组别
    for j in range(n): #n
        tmp1 = random.gauss(mu1, sigma1)
        tmp2 = random.gauss(mu2, sigma2) * np.random.binomial(1, p)
        ans[i] = ans[i] + tmp1 + tmp2
    u.append((1/((n*DZ) ** 0.5)) * (ans[i] - n*EZ))

plt.hist(u, bins = 50, color = "#F8BBD0")
#plt.hist(nums2, bins = 200, color = "#4CAF50")
plt.title('U频率直方图 (n=1000)')
plt.show()