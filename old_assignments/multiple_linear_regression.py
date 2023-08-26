# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 01:12:09 2019

@author: TANMEY
"""

#importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#importing data
startup=pd.read_csv("T:/datasets/udemy/50_Startups.csv")
X = startup.iloc[:, :-1].values
Y = startup.iloc[:,4].values

#used to check whether missing values are there or not
# print(startup.isnull().sum())


#Dealing with categorical variables
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import  OneHotEncoder
columntransformer=ColumnTransformer([('dummy variable',OneHotEncoder(),[3])],remainder='passthrough')
X= np.array(columntransformer.fit_transform(X), dtype=np.float)
