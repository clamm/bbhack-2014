from __future__ import (absolute_import, division, print_function,
                        with_statement)

__author__ = 'lfoppiano'

from stemming.porter2 import stem
from bbhack.plotter import Plotter
import operator

termFreq = {}
counter = 0
maxLen = 100


class Algorithms:
    def __init__(self):
        self.plotter = Plotter()


    def computeHeavyHitter(self, tag):
        tag = tag.lower()
        tag = stem(tag)

        if tag in termFreq.keys():
            termFreq[tag] += 1
        else:
            if len(termFreq) > maxLen:
                sortedTermFreq = sorted(termFreq.iteritems(), key=operator.itemgetter(1), reverse=True)
                last = sortedTermFreq[-1]

                print("removing " + str(last))
                del termFreq[last[0]]
                termFreq[tag] = last[1] + 1
            else:
                termFreq[tag] = 1

        self.sortedTermFreq = sorted(termFreq.iteritems(), key=operator.itemgetter(1), reverse=True)
        #global counter
        #self.plotter.plot(self.sortedTermFreq, counter)
        #counter += 1

        print(self.sortedTermFreq)




    #def computeSketch
