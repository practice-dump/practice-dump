# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 05:12:44 2020

@author: TANMEY
"""

import numpy as np
from numpy import linalg as LA
A = np.array([[1,1],[1,2],[1,3]])

def column_convertor(x):
    x.shape = (1, x.shape[0])
    return x
def householder_logic(x):
    e1=np.zeros(x.shape[1])
    e1[0]=1
    v_temp=LA.norm(x,2)*e1
    if v_temp[0]<0:
        v_temp=-v_temp
    v=x+v_temp
    p=np.matmul(v.T,v)
    l=LA.norm(v,2)**2
    H=np.identity(x.shape[1])-2*(np.matmul(v.T,v)/(LA.norm(v,2)**2))
    return H
    
def householder_service(A):
    m,n = A.shape
    Q=np.identity(m)
    R=np.copy(A)
    for i in range(0,n):
        x=R[i:,i]
        x=column_convertor(x)
        H=householder_logic(x)
        Q_temp=np.identity(m)
        Q_temp[i:,i:]=H
        R=np.matmul(Q_temp, R)
        Q=np.matmul(Q, Q_temp)
    return (Q,R)
    
Q_H,R_H=householder_service(A)
    
