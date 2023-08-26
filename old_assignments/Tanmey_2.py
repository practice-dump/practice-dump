# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 18:42:14 2019

@author: TANMEY
"""
#run these import statements first to execute code written below
import numpy as np
import sympy as sp
from scipy.optimize import fsolve
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x=sp.symbols('x')

#question1
final_result=0
for i in range(0,11):
    next_term=sp.diff(sp.cos(x)**-1,x,i).subs(x,0)*(x)**i/(math.factorial(i))
    final_result+=next_term
print(final_result)

#question2
def seriescalc(n):
    sum=0
    for i in range(1,n+1):
        sum+=(-1)**(i+1)/i
        
    ln2=math.log(2)
    
    epislon=ln2-sum
    return epislon
series="1-(1/2)+(1/3)-1/4,......"
print("When we take upto 100 terms the difference between "+series+ " and ln2 is",seriescalc(100))
print("When we take upto 1000 terms the difference between" +series+ "and ln2 is",seriescalc(1000))


#question3
def powerseries(k,z):
    y=0
    for i in range(0,k+1):
        y=y+(-1)**i*(z)**(2*i)/(math.factorial(i))**2
    return y
z=np.linspace(-8,8,100)
plt.ylim(-5,5)
plt.plot(z,powerseries(10,z),'g')
plt.plot(z,powerseries(20,z),'r')
plt.plot(z,powerseries(40,z),'b')

#the the plot of f40(x) for 8 < x < 8 visually indistinguishable from the plot of f20(x) over the same domain
#because the terms which are present in f40 but not in f20 approach zero due to n factorial squared.


#question 4

theta=np.linspace(-5*np.pi,5*np.pi,1000)
#question4a
r=np.sin(theta)
plt.polar(theta,r)
#question4b
r2=4*np.sin(theta)-2
plt.polar(theta,r2)
#question4c
r3=(np.sin(2*theta))**0.5
plt.polar(theta,r3)

#question 5
#question 5a
fig = plt.figure()
ax = fig.gca(projection='3d')
t=np.linspace(-5*np.pi,5*np.pi,100)
x=np.cos(t)
y=np.sin(t)
z=t/2
ax.plot(x,y,z, label='(cos t; sin t; t/2)')
ax.legend()


#question 5b

fig = plt.figure()
ax = fig.gca(projection='3d')
t2=np.linspace(-5,5,100)
x=t2
y=t2**2
z=t2**3
ax.plot(x,y,z,label='(t,t^2,t^3)')
ax.legend()


#question 6
t=np.linspace(0,4*np.pi,100)
x1=2*t-2*np.sin(t)
y1=2-2*np.cos(t)
x2=2*t-np.sin(t)
y2=2-np.cos(t)

plt.plot(x1,y1,'g')
plt.plot(x2,y2,'b')
def equations(p):
    x, y = p
    return (2*x-2*np.sin(x)-(2*y-np.sin(y)),np.cos(y)-2*np.cos(x))

a, b =  fsolve(equations, (11,11))

print(a,b)

# by keeping guess (1,1) we get points a1=1.0918235838014578,b1=0.39826429758283133
#so by changing the guess we would find other points 
# by keeping guess (5,5) we get points a2=5.191361723373371 ,b2=5.884921009604868
# by keeping guess (6.7,6.7) we get points a3=7.375008890985416,b3=6.681449604759625
# by keeping guess (11,11) we get points a4=11.474547030552126,b4=12.16810631677326
a1=1.0918235838014578
b1=0.39826429758283133
a2=5.191361723373371
b2=5.884921009604868
a3=7.375008890985416
b3=6.681449604759625
a4=11.474547030552126
b4=12.16810631677326
plt.plot(x1,y1,'g')
plt.plot(x2,y2,'b')
plt.scatter(2*(a1-np.sin(a1)),2*(1-np.cos(a1)), color='black',s=100 )
plt.scatter(2*(a2-np.sin(a2)),2*(1-np.cos(a2)), color='black',s=100 )
plt.scatter(2*(a3-np.sin(a3)),2*(1-np.cos(a3)), color='black',s=100 )
plt.scatter(2*(a4-np.sin(a4)),2*(1-np.cos(a4)), color='black',s=100 )



























    