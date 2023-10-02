import matplotlib.pyplot as plt
from matplotlib import pyplot
import numpy as np
import pandas as pd
from numpy import genfromtxt

#import CSV file
m = genfromtxt('iris_data.csv', delimiter=',', dtype= float )

x1 =[]
y1 = []

for i  in range( 1 , 150) :
    x1.append(m[i][4])
    y1.append(m[i][3])


fig = plt.figure(figsize = (16,9))
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
x = [min(x1) , max(x1)]
y = np.interp(x, x1, y1)
ax1.scatter(x1, y1, marker='x')
ax1.errorbar(x1, y1, yerr=0.02, xerr = 0.01, color = 'k', linestyle = 'None')
ax1.plot(x,y,'r')
ax1.grid() # делаем сетку


plt.show()