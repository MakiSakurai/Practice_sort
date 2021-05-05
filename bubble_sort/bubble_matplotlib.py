#!usr/bin/env python
# -*- coding: utf-8 -*-

import math
import numpy as np
import matplotlib.pyplot as plt

rand = np.random.randint(1, 100, 100)
x = np.arange(len(rand))
n = len(rand)
for i in range(n - 1):
    for j in range ((n - i) - 1):
        if rand[j] > rand[j + 1]:
            rand[j], rand[j + 1] = rand[j + 1], rand[j]
            line = plt.bar(x, rand, color='blue')
            plt.pause(0.01)
            line.remove()
            print(rand)
plt.bar(x, rand, color='blue')
plt.show()
print(rand)