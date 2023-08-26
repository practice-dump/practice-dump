# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 01:28:20 2019

@author: TANMEY
"""
#importing libraries which I would hopefully require
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#importing data
from sklearn.datasets import load_boston
dataset=load_boston()

#understanding what is available in data
print(dataset.keys())

#segregation of independent and dependent variables
dataset_values=dataset['data']
target_variable=dataset['target']
# print(dataset['feature_names'])
# print(dataset['DESCR'])
#In descr it is written no missing attribute so we won't be doing that but should be checked

#plotting different graphs to see pairwise relationship of independent variables and median pricing
sns.distplot(target_variable,bins=40)
df1=pd.DataFrame(dataset_values,columns=dataset['feature_names'])
df1['Price']=target_variable
correlation_matrix=df1.corr().round(2)
plt.figure(figsize=(16, 6))
sns.heatmap(correlation_matrix,annot=True)# if we remove annot=True the we won't get numbers in heatmap
# print(correlation_matrix.loc['Price'])
#As we can see the correlation of RM and LSTAT  high with Price and their own correaltion is low therefore
#we would use only these 2 variables
X=pd.DataFrame(np.c_[df1['RM'],df1['LSTAT']],columns=['RM','LSTAT'])
Y=target_variable


#separation of training and test datasets
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=0)


#fitting linear regression to model
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train, Y_train)


#predicting result

Y_pred=regressor.predict(X_test)
plt.scatter(Y_test, Y_pred)

#evaluation
from sklearn.metrics import mean_squared_error,r2_score
rmse=np.sqrt(mean_squared_error(Y_test, Y_pred))
r2=r2_score(Y_test, Y_pred)

#just to check the evaluation metrics we would take whole data
regressor2=LinearRegression()
ind_train,ind_test,dep_train,dep_test=train_test_split(dataset_values,target_variable, test_size=0.2,random_state=0)
regressor2.fit(ind_train,dep_train)
dep_pred=regressor2.predict(ind_test)
rmsewhole=np.sqrt(mean_squared_error(dep_test, dep_pred))
r2whole=r2_score(dep_test, dep_pred)

