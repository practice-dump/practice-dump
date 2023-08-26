# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 18:35:16 2019

@author: TANMEY
"""



def merge(l1,l2):
    finalist=[]
    while(l1!=[] and l2!=[]):
        if(l1[0]<=l2[0]):
            finalist.append(l1[0])
            l1.pop(0)
        else:
            finalist.append(l2[0])
            l2.pop(0)
    return finalist+l1+l2
#merge([1,3,5,7,9],[2,4,6,8,0])


def mergesort(l):
    if(len(l)<=1):
        return l
    mid=len(l)//2
    lefthalf=mergesort(l[:mid])
    righthalf=mergesort(l[mid:])
    return(merge(lefthalf,righthalf))
    
mergesort([1,3,5,7,9,2,4,6,8,0])


#merging two list recursion used
def merger(l1,l2):
    ans=[]
    if(len(l1)==0):
        return ans+l2
    elif(len(l2)==0):
        return ans+l1
    if l1[0] <= l2[0]:
        ans.append(l1[0])
        l1.pop(0)
    else:
        ans.append(l2[0])
        l2.pop(0)
    ans=ans+merger(l1,l2)
    return ans
y=merger([1,3,5,7,9],[0,2,4,6,8])  



def mergesortnested(l):
    if(len(l)<=1):
        return l
    mid=len(l)//2
    lefthalf=mergesort(l[:mid])
    righthalf=mergesort(l[mid:])
    def mergenested(l1,l2):
        finalist=[]
        while(l1!=[] and l2!=[]):
            if(comparisonfunction(l1[0],l2[0])):
                finalist.append(l1[0])
                l1.pop(0)
            else:
                finalist.append(l2[0])
                l2.pop(0)
        return finalist+l1+l2
    
    return(mergenested(lefthalf,righthalf))
    
    
def comparisonfunction(a,b):
    (y1,x1)=a
    (y2,x2)=b
    return (y1,x1)<=(y2,x2)
mergesortnested([1,3,5,7,9,2,4,6,8,0])



  