import matplotlib.pyplot as plt
from matplotlib import pyplot
import numpy as np
import pandas as pd

from numpy import genfromtxt

#import CSV file
m = genfromtxt('iris_data.csv', delimiter=',', dtype= float )

k =0
n = 0
q = 0
for i in range(150) :
    if m[i , 4] < 1.2 :
        k += 1/150
    if m[i , 4] > 1.2 and m[i , 4] < 1.5  :
        n += 1/150
    if m[i , 4] > 1.5 :
        q += 1/150
print(k,n,q)

w = 1/3
e = 1/3
r = 1/3

fig = plt.figure(figsize = (16,9))
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

ax1.pie([k , n ,q])
ax2.pie([ w , e ,q])

plt.show()