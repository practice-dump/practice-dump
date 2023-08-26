# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 01:12:14 2019

@author: TANMEY
"""

#importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt


#importing data
dataset=pd.read_csv("T:/datasets/udemy/Salary_Data.csv")

#division of dependent and independent variables
exp=dataset.iloc[:,:-1].values
sal=dataset.iloc[:,1].values

#division of data into training and testing
#segregation of data into training and testing data
from sklearn.model_selection import train_test_split
exp_train,exp_test,sal_train,sal_test=train_test_split(exp,sal,test_size=0.2,random_state=0) 


#fitting linear regression to model
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(exp_train, sal_train)

#predicting test results
sal_pred=regressor.predict(exp_test)

#visualizing the model
# plt.scatter(exp, sal, color='green')
plt.scatter(exp_test, sal_test, color='red')
plt.plot(exp_train,regressor.predict(exp_train),color='blue')
plt.title("Salary vs Experience")
plt.xlabel("Experience")
plt.ylabel("Salary")

#just checking average deviation for own satisfaction
temp=0
for i in range(len(sal_pred)):
    temp+=abs(sal_pred[i]-sal_test[i])
avg_deviation=temp/len(sal_pred)

#predicting salary of an employee with 15 years of experience.
temparray=[[15]]
print(regressor.predict(temparray))


