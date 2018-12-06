#!/usr/bin/env python

from plot import plot
x= [2,-3, 4, 5.3, 9.6, -12, -8.4, 2.4, 10, 3.4]
x.sort()
y= [2,-3, 4, 5, 4.6, -1.5, -8.4, 2.4, 10, 3.4]
y_err= [0.2, 0.001, 0.02, 0.01, 0.06, 0.12, 0.32, 0.04, 0.3, 0.09]
y1 = [-2,-3, 5.4, 5, 4.1, -1.3, -6.4, 2.8, 12, 3.2]
plot (x, y, 'random numbers', 'other random numbers','scatter',y1, y_err,'test', 4 )

