# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:13:44 2019

@author: TANMEY
"""

#insertioninto sorted list
def insertion(n,l):
    for i in range(0,len(l)):
        if(l[i]>=n):
            return l[0:i]+[n]+l[i:]
    return l+[n]
    
#Sir's way
#def insert(v,ls):
#    i = 0
#    N = len(ls)
#    while (i < N) and (ls[i] <= v):
#        i = i+1
#    return(ls[0:i]+[v]+ls[i:])


def insertionsort(l):
    ans=[]
    for each in l:
        ans=insertion(each,ans)
    return ans
#insertionsort([1,7,9,6,2,5])
    
print(insertionsort([("a",1),("b",10),("c",1),("d",1),("b",2),("c",2),("e",1),("c",3)]))


#insertionsort uses second argument to order first
def insertionadvanced(v,ls):
    i=0
    N=len(ls)
    while (i < N) and comparsionfunction(ls[i], v):
        i=i+1
    return (ls[0:i]+[v]+ls[i:])

def insertionsortadvanced(ls):
    ans=[]
    for each in ls:
        ans=insertionadvanced(each,ans)
    return (ans)

def comparsionfunction(a,b):
    (x1,y1) = a
    (x2,y2) = b
    return ((y1,x1) <= (y2,x2))


print(insertionsortadvanced([("a",1),("b",10),("c",1),("d",1),("b",2),("c",2),("e",1),("c",3)]))
