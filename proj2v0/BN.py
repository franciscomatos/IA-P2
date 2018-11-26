# -*- coding: utf-8 -*-

"""
Created on Mon Oct 15 15:51:49 2018

@author: mlopes
"""

import numpy as np
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

                

    
class BN():
    # gra - parents array
    # prob - nodes array
    def __init__(self, gra, prob):
        self.gra = gra
        self.prob = prob
        

    def computePostProb(self, evid):
        pass
               
        return 0
        
        
    def computeJointProb(self, evid):
        p = 1
        i = 0

        for prob in self.prob:
            p *= prob.computeProb(evid)[evid[i]]
            i += 1
        
        return p

if __name__ == "__main__":
    ev = (1,1,1,1,1)
    
    p1 = Node( np.array([.001]), [] )
    print(p1.computeProb(ev))

    p3 = Node( np.array([[.001,.29],[.94,.95]]), [0,1] )
    print(p3.computeProb(ev))
    ev = (0,0,1,1,1)

    print(p3.computeProb(ev))
    ev = (0,1,1,1,1)
    print(p3.computeProb(ev))

    ev = (1,0,1,1,1)
    print(p3.computeProb(ev))

    ev = (1,1,1,1,1)
    print(p3.computeProb(ev))

    prob = [p1,p2,p3,p4,p5]

    gra = [[],[],[0,1],[2],[2]]
    bn = BN(gra, prob)

    jp = []
    for e1 in [0,1]:
        for e2 in [0,1]:
            for e3 in [0,1]:
                for e4 in [0,1]:
                    for e5 in [0,1]:
                        jp.append(bn.computeJointProb((e1, e2, e3, e4, e5)))

    print("sum joint %.3f (1)" % sum(jp))
