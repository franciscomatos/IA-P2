# -*- coding: utf-8 -*-

"""
Created on Mon Oct 15 15:51:49 2018

@author: mlopes
"""

import numpy as np
import itertools as it
np.set_printoptions(precision=20, suppress=True)

class Node():
    def __init__(self, prob, parents = []):
        self.parents = parents
        self.prob = prob
    
    def computeProb(self, evid):
        nParents = len(self.parents)
        p = self.prob # gonna select a probability from the array
        i = 0
        if nParents == 0: 
            return [1 - self.prob[0], self.prob[0]]
        else:
            for parent in self.parents:
                e = evid[parent] # relevant evid value
                p = p[e]         # if e = 0, first parent false, index = 0
                                 # if e = 1, first parent true, index = 1
            return [1 - p, p]

                

def isPost(n):
    return n == -1

def isUnknown(n):
    return isinstance(n, list)

# given the original evid, the posterior and unknown variables index, returns a list of all possible evids 
# evid - original evid
# x - posterior variable index
# y - unknown variables index
# val - 1 or 0, depending on whether the posterior variable is true or not 
def computeEvids(evid, x, y, val):
    evidsList = []

    # list of all possible combinations of the unknown variables
    l = list(it.product([0,1], repeat=len(y)))

    for possibility in l:
        aux = list(evid)
        aux[x[0]] = val # changes the posterior variable
        for i in range(len(y)): # changes the unknown variables
            aux[y[i]] = possibility[i]
        evidsList.append(aux)

    
    return evidsList

        

class BN():
    def __init__(self, gra, prob):
        self.gra = gra # parents array
        self.prob = prob # nodes array
        

    def computePostProb(self, evid):
        x, y, e = [], [], []
        num, i , p, p2, alpha = 0, 0, 0, 0, 0
        # reads the index of the relevant nodes
        for ev in evid:
            if isUnknown(ev):
                y.append(i)
            elif isPost(ev):
                x.append(i)
            else:
                e.append(i)
            i += 1

        numEv = computeEvids(evid, x, y, 1)
        denEv = computeEvids(evid, x, y, 0)

        for e in numEv:   
            p += self.computeJointProb(e)

        for e in denEv:
            p2 += self.computeJointProb(e)

        alpha = p + p2
        return p/alpha
            

        
        
    def computeJointProb(self, evid):
        p = 1
        i = 0

        for prob in self.prob:
            p *= prob.computeProb(evid)[evid[i]]
            i += 1
        
        return p

