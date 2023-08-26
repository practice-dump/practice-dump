# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 23:10:32 2019

@author: TANMEY
"""
#src udemy https://www.udemy.com/course/machinelearning/learn/lecture/6151022#questions
#datapreprocessing 
#by pressing F5 the file is saved and executed.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


dataset=pd.read_csv("T:/datasets/Data.csv")
X = dataset.iloc[:, :-1].values #here we have created separate matrix for independent variables.
#iloc [a,b] a represents which rows we want to take and b tells which col we want to take. 
#so by [:,:-1] we say take all rows and all columns except last one(denoted by -1)
x=dataset.iloc[:, :-1] # if we don't write .values the we will not be able to access the values
Y=dataset.iloc[:,3].values # here Y is dependent variable so we are taking 4th column(index=3)


#dealing with missing values and replacing it with mean for instance we can change to median also and some other 
#value as per our choice
from sklearn.impute import SimpleImputer
imp=SimpleImputer(missing_values=np.nan,strategy="mean")
imp=imp.fit(X[: ,1:3])
X[: ,1:3]=imp.transform(X[:,1:3])


#Dealing with categorical variables
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
columntransformer=ColumnTransformer([('dummy variable',OneHotEncoder(),[0])],remainder='passthrough')
X= np.array(columntransformer.fit_transform(X), dtype=np.float)
labelencoder_Y=LabelEncoder()
Y=labelencoder_Y.fit_transform(Y)


#segregation of data into training and testing data
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=0) 
#here we have kept random state =0 first of all it can be kept equal to anything
#second we have kept it here so we get the same split everytime we run it 
#if we change random_state=1 we get diff results


#featurescaling
#we do feature scaling because if algo depends upon eucledian distance and if we don't do feature scaling then
#our model be affected by large values of one column 
#second it converges faster after applying standardisation
from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
X_train=sc_X.fit_transform(X_train) 
X_test=sc_X.transform(X_test) # we already fitted with X_train so no need to do that again
#here we have small dilema whether to standardised categorical variables or not. 
#if we standardised we have more accuracy but we lose the interpretation of dummy variables.

#for regession section we would have to apply feature selection on dependent variables.









