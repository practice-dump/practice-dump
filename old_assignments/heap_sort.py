# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 14:42:43 2019

@author: TANMEY
"""

#insertion in heaps

L=[]
N=0

def insert(x):
   global L,N
   L.append(x)
   N=N+1
   curr=N-1
   while(curr>0 and L[(curr-1)//2]<L[curr]):
       L[(curr-1)//2],L[curr]=L[curr],L[(curr-1)//2]
       curr=(curr-1)//2
       
       
for i in [2,3,1,4,5,2,6,3]:
    insert(i)
print(L)



def deletemax():
    global L,N
    if(L==[]):
        return None
    N=N-1
    ans=L[0]
    L[0]=L.pop()
    curr=0
    while(curr<N):
        curr1=curr*2+1
        curr2=curr*2+2
        if(curr1==N):
            swapper=curr1
        elif(curr1<N):
            if(L[curr1]>L[curr2]):
                swapper=curr1
            else:
                swapper=curr2
        else:
            return ans
            
        if(L[swapper]>L[curr]):
            L[swapper],L[curr]=L[curr],L[swapper]
            curr=swapper
        else:
            return ans
     
print(deletemax())
        
        