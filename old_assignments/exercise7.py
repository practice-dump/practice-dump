# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 13:51:23 2019

@author: TANMEY
"""

import numpy as np
import matplotlib.pyplot as plt
def flipCoin():
    a=np.random.randint(0,2)
    return a

def countHeads(t):
    counter=0
    for i in range(0,t):
        c=flipCoin()
        if(c==1):
            counter+=1
    return counter

t=5
m=5000
n=4000

def experiment(t,m,n):
    E=np.empty(m*n,dtype=np.int64)
    for i in range(0,m*n):
        temp1=countHeads(t)
        E[i]=temp1
    E=E.reshape(m,n)
    F=np.mean(E,axis=1)
    plt.hist(F)
    return F




experiment(t,m,n)
        
    



