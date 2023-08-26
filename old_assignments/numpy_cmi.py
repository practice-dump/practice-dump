# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 16:21:10 2019

@author: TANMEY
"""

import numpy as np
a=np.array([1,2,3,4,5])
print(a)
print(type(a))
b=np.array([[2,3],[1,5],[6,9]])
b.ndim
b.shape
b.size
print(b.T)
print(a.T)
print(b.transpose())
c=np.array([1,0,9,3,4])
d=a*c
c=c.transpose()
d=b.transpose()
e=b@d
c=np.zeros([2,2])
e=np.empty([3,3,3])
e=np.random.random([3,3,4])
b=np.array([range(1,20),range(1,20)])

def f(x,y,z):
    return x+y+z
a = np.fromfunction(f,[4,5,6])
print(a)

np.array(np.arange(0,5,.35))
type(np.arange(0,3,2))
a=np.array([np.linspace(0,5,18)]) # split in 18 parts
print(a.reshape([3,6]))
print(a)
b.ravel()
b.reshape([2,18])
b.sum(axis=1)
b.cumsum(axis=1)
np.mean(b,axis=0)
x = np.arange(1, 7).reshape(2, 3)
x.flat[3]
x=x.flat





