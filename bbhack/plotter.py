__author__ = 'lfoppiano'

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Plotter:
    def __init__(self):
        # First set up the figure, the axis, and the plot element we want to animate
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        #self.ax = plt.axes(xlim=(0, 2),ylim=(0, 2))
        #self.line, = self.ax.plot([], [], lw=2)

    def animate(self, frame):
        print self.dataSource.getSortedTermFreq()
        x = np.linspace(0, 2, 1000)
        #y = hashtags[1] #counter of hashtag

        #line, = self.ax.plot([], [], lw=2)
        #line.set_data(x, y)
        return None,

    def plot(self, sortedTermFreq, counter):
        x = counter
        y = sortedTermFreq[0][1]


        line1, = self.ax.plot(x, y, 'r-')
        line1.set_ydata(sortedTermFreq[0][1])
        self.fig.canvas.draw()
        plt.show(block=False)




