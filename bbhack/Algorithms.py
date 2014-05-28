from __future__ import (absolute_import, division, print_function,
                        with_statement)

__author__ = 'lfoppiano'

from stemming.porter2 import stem
# from bbhack.plotter import Plotter
import operator
import random

termFreq = {}
counter = 0
maxLen = 100
nbBins = 4
nbHashfunctions = 5


class Algorithms:
    def __init__(self):
        # self.plotter = Plotter()
        self.hashDict = self.createHashDict()
        self.counterMatrix = self.createMatrix()

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
        # global counter
        # self.plotter.plot(self.sortedTermFreq, counter)
        #counter += 1

        print(self.sortedTermFreq)

    def computeSketch(self, tag):
        tag = tag.lower()
        binIndices = self.getBinIndices(tag)
        self.incrementBin(binIndices)

    def getSketchFor(self, tag):
        binIndices = self.getBinIndices(tag)
        sketches = []
        for hash, bin in enumerate(binIndices):
            sketches.append(self.counterMatrix[hash][bin])
        return min(sketches)

    def incrementBin(self, binIndices):
        for hash, bin in enumerate(binIndices):
            self.counterMatrix[hash][bin] += 1

    def getBinIndices(self, tag):
        hashValues = []
        for hashFunction in self.hashDict.values():
            hashValues.append(hashFunction(tag))
        binIndices = [int(elem % nbBins) for elem in hashValues]
        return binIndices

    def createMatrix(self):
        matrix = [[0 for x in xrange(nbBins)] for x in xrange(nbHashfunctions)]
        return matrix

    def createHashDict(self):
        hashDict = {}
        for i in range(nbHashfunctions):
            hashDict[i] = self.hashFunction(i)
        return hashDict

    def hashFunction(self, n):
        _memomask = {}
        mask = _memomask.get(n)
        if mask is None:
            random.seed(n)
            mask = _memomask[n] = random.getrandbits(32)

        def myhash(x):
            return hash(x) ^ mask

        return myhash


if __name__ == '__main__':
    Algorithms().computeSketch('bla')