# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 18:04:54 2019

@author: TANMEY
"""


def selectionsort(l):
    pos=0
    while pos<len(l):
        for i in range(pos+1,len(l)):
            if(l[pos]>l[i]):
                l[pos],l[i]=l[i],l[pos]
        pos+=1
    return l
y=selectionsort([4,69,1,54,7,3,78,32])



def selectionsortadvanced(ls):
    pos=0
    while pos<len(ls):
        for i in range(pos+1,len(ls)):
            if(comparisonfunction(ls[pos],ls[i])):
                ls[pos],ls[i]=ls[i],ls[pos]
        pos+=1
    return ls


def comparisonfunction(a,b):
    (x1,y1)=a
    (x2,y2)=b
    if(y1>y2):
        return True
    else:
        return False
    
    
selectionsortadvanced([("a",1),("b",10),("c",1),("d",1),("b",2),("c",2),("e",1),("c",3)],comparisonfunction)
    