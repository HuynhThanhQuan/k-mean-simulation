# -*- coding: utf-8 -*-
"""
Created on Mon May 21 13:10:29 2018

@author: HUQ81HC
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

np.random.seed(0)

N = 50
x_init = np.random.rand(N)
y_init = np.random.rand(N)

x = np.random.rand(2)
y = np.random.rand(2)

'''
dis_x0 = np.array([x[0] - x0 for x0 in x_init])
dis_x1 = np.array([x[1] - x1 for x1 in x_init])
dis_y0 = np.array([y[0] - y0 for y0 in y_init])
dis_y1 = np.array([y[1] - y1 for y1 in y_init])
dis_p0 = np.array([np.sqrt(dis_x0[i]**2 + dis_y0[i]**2) for i in range(50)])
dis_p1 = np.array([np.sqrt(dis_x1[i]**2 + dis_y1[i]**2) for i in range(50)])

clu = []

for i in range(50):
    if dis_p0[i] < dis_p1[i]:
        clu.append(0)
    else:
        clu.append(1)
    

for i in range(50):
    if clu[i] == 0:
        c ='b'
    else:
        c ='r'
    plt.scatter(x_init[i], y_init[i], marker='o', color=c)

plt.scatter(x[0], y[0], s= 100 , marker='x', color='b')
plt.scatter(x[1], y[1], s= 100 , marker='x', color='r')
plt.show()
'''
    
class K_Mean_Animation:
    def __init__(self, points, k):
        self.x_points = points[0]
        self.y_points = points[1]
        self.p0 = (k[0][0], k[1][0])
        self.p1 = (k[0][1], k[1][1])
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1, 1, 1)
    def get_axes(self):
        return self.ax
    def plot(self):
        self.ax.scatter(self.x_points, self.y_points, marker = 'o', color = 'g')
        self.ax.scatter(self.p0[0], self.p0[1], s= 100 , marker='x', color='b')
        self.ax.scatter(self.p1[0], self.p1[1], s= 100 , marker='x', color='r')
    def find_vicinity(self):
        dis_x0 = np.array([self.p0[0] - x0 for x0 in self.x_points])
        dis_x1 = np.array([self.p1[0] - x1 for x1 in self.x_points])
        dis_y0 = np.array([self.p0[1] - y0 for y0 in self.y_points])
        dis_y1 = np.array([self.p1[1] - y1 for y1 in self.y_points])
        dis_p0 = np.array([np.sqrt(dis_x0[i]**2 + dis_y0[i]**2) for i in range(50)])
        dis_p1 = np.array([np.sqrt(dis_x1[i]**2 + dis_y1[i]**2) for i in range(50)])
        self.clu = []
        for i in range(50):
            if dis_p0[i] < dis_p1[i]:
                self.clu.append(0)
            else:
                self.clu.append(1)
        #self.ax.cla()
        for i in range(50):
            if self.clu[i] == 0:
                c ='b'
            else:
                c ='r'
            self.ax.scatter(self.x_points[i], self.y_points[i], marker='o', color=c)
        self.ax.scatter(self.p0[0], self.p0[1], s= 100 , marker='x', color='b')
        self.ax.scatter(self.p1[0], self.p1[1], s= 100 , marker='x', color='r')
    def find_centeroid(self):
        self.ax.scatter(self.p0[0], self.p0[1], s= 100 , marker='x', color='w')
        self.ax.scatter(self.p1[0], self.p1[1], s= 100 , marker='x', color='w')
        x0_center = np.average([self.x_points[i] for i in range(50) if self.clu[i] == 0])
        x1_center = np.average([self.x_points[i] for i in range(50) if self.clu[i] == 1])
        y0_center = np.average([self.y_points[i] for i in range(50) if self.clu[i] == 0])
        y1_center = np.average([self.y_points[i] for i in range(50) if self.clu[i] == 1])
        self.p0 = (x0_center, y0_center)
        self.p1 = (x1_center, y1_center)
        self.ax.scatter(self.p0[0], self.p0[1], s= 100 , marker='x', color='b')
        self.ax.scatter(self.p1[0], self.p1[1], s= 100 , marker='x', color='r')
        
if __name__ == '__main__':
    test = K_Mean_Animation((x_init, y_init), (x,y))
    test.plot()    
    ax = test.get_axes()
    bnext = Button(ax, 'Next')