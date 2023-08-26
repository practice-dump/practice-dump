# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 18:16:07 2019

@author: TANMEY
"""

def rootsort(L):
    N=len(L)
    rn=0
    while(rn*rn<N):
        rn+=1
    listoflist=[]
    lengthlist=[]
    for i in range(0,rn):
        listoflist.append([])
        lengthlist.append(0)
        
        
        def insert(x):
            nonlocal rn,listoflist,lengthlist
            i=0
            while(i < rn and lengthlist[i]==rn): #this means we are checking first list if it is full then using i+1 we check next list
                i+=1
            if(i==rn):
                print("no empty list is available please try later")
                return
            j=0
            while(j<lengthlist[i] and listoflist[i][j]<x):
                j+=1
            listoflist[i].insert(j,x) #inserts x at (i,j)
            lengthlist[i]=lengthlist[i]+1
            
        def deletemax():
            nonlocal rn,listoflist,lengthlist
            maximumlist=[]
            i=0
            while(i<rn and lengthlist[i]>0):
                maximumlist.append(listoflist[i][-1],i)
                i=i+1
            ans,index=max(maximumlist)
            listoflist[index].pop()
            lengthlist[index]=lengthlist[i]-1
            return ans
        
        
        for e in L:
            insert(e)
        finalsortedlist=[]
        for i in range(0, len(L)):
            finalsortedlist.append(deletemax())
        print(finalsortedlist)

        
rootsort([1,5,3,7,6,8,9])        
                
            