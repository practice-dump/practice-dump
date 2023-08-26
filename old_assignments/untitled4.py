# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 23:05:36 2019

@author: TANMEY
"""

class BTree():
    def __init__(self,v,l=None,r=None):
        self.value=v
        self.left=l
        self.right=r
    
    def __str(self,v):
        if v:
            return(str(v))
        return "E"
    def __str__(self):
        return("("+self.__str(self.value)+" "+ self.__str(self.left)+" "+ self.__str(self.right)+")")
        
        
    def preorder(self):
        ans=[self.value]
        if self.left:
            ans=ans+self.left.preorder()
        if self.right:
            ans=ans+self.right.preorder()
        return ans
    
    def inorder(self):
        ans=[]
        if self.left:
            ans=ans+self.left.inorder()
        ans=ans+[self.value]
        if self.right:
            ans=ans+self.right.inorder()
        return ans
    
    
    def postorder(self):
        ans=[]
        if self.left:
            ans=ans+self.left.postorder()
        if self.right:
            ans=ans+self.right.postorder()
        ans=ans+[self.value]
        return ans
    
class BSTree(BTree):
    def __init__(self,v=None):
        self.value = v
        self.left = None
        self.right = None
    
    def search(self,v):
        if self.value==v:
            return True
        elif(self.value>v and self.left):
            self.left.search(v)
        elif (self.value<v and self.right):
            self.right.search(v)
        return False
    
    def isEmpty(self):
        if self.value==None:
            return True
        return False
    
    
    def insert(self,v):
        if self.isEmpty():
            self.value=v
            return
        if self.value==v:
            return 
        elif(self.value>v and self.left):
            self.left.insert(v)
        elif(self.value>v):
            self.left=BSTree(v)
        elif (self.value<v and self.right):
            self.right.insert(v)
        elif (self.value<v):
            self.right=BSTree(v)
            
            
    def deletemax(self):
        if self.isEmpty():
            return None
        if self.right:
            ans=self.right.deletemax()
            if self.right.isEmpty():
                self.right=None
        else:
            ans=self.value
            if not self.left:
                self.value=None
                
            else:
                self.value=self.left.value
                self.left=self.left.left
                self.right=self.left.right
        return ans
    
            
            
    def delete(self,v):
        if self.isEmpty():
            return None
        if(self.value>v and self.left):
            self.left.delete(v)
            if self.left.isEmpty():
                self.left=None
        elif(self.value>v):
            return None
        elif(self.value<v and self.right):
            self.right.delete(v)
            if self.right.isEmpty():
                self.right=None
        elif(self.value<v):
            return None
        elif(self.value==v):
            if not self.left and not self.right:
                self.value=None
            elif( not self.left):
                self.value=self.right.value
                self.left=self.right.left
                self.right=self.right.right
            else:
                self.value=self.left.deletemax()
                if self.left.isEmpty():
                    self.left=None
         return 
       
        
        
            
        
    
        
x = BSTree(5)
x.insert(6)
x.insert(8)
x.insert(7)
x.insert(3)
x.insert(4)
x.insert(5)
print(x)
x.delete(0)
print(x.search(3))
print(x.search(9))
print(x.inorder())