import numpy as np
import matplotlib.pylab as pl

file = open('plot/fcPlot.txt', 'r')
x1 = []
y1 = []
i = 1
for l in file.readlines():
    l.rstrip()
    x1.append(float(l))
    y1.append(i)
    i += 1
file.close()


file = open('plot/saPlot.txt', 'r')
x2 = []
y2 = []
i = 1
for l in file.readlines():
    l.rstrip()
    x2.append(float(l))
    y2.append(i)
    i += 1
file.close()


pl.figure()
pl.plot(y1, x1, label='First Choice')
pl.plot(y2, x2, label='Simulated Annealing')
pl.xlabel('Number of Evaluations')
pl.ylabel('Tour cost')
pl.title('Search cost for each algorithm')
pl.legend()
pl.show()