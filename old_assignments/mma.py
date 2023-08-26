# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 00:42:27 2019

@author: TANMEY
"""
import numpy as np
import scipy.integrate as intg
import sympy as sp
import matplotlib.pyplot as plt
x=sp.symbols('x')

#question1
theta=np.linspace(0,2*np.pi,10000)
#question1a
plt.plot(theta,np.sin(theta))
plt.title('Sine Wave')
plt.xlabel('Theta in Radians')
plt.ylabel('sin(theta)')
plt.grid(True, which='both')
#question1b
plt.plot(theta,np.tan(theta))
plt.ylim(-5, 5)
plt.title('Tan Wave')
plt.xlabel('Theta in Radians')
plt.ylabel('tan(theta)')
plt.grid(True, which='both')
#question 1c
theta2=np.linspace(-5,5,1000)
plt.plot(theta2,np.cosh(theta2))
plt.title('Graph for cosh(x)')
plt.xlabel('x')
plt.ylabel('cosh(theta)')
plt.grid(True, which='both')
#question 1d
plt.plot(theta2,np.exp(-1*theta2**2))
plt.title('Graph of exp(-x^2)')
plt.xlabel('x')
plt.ylabel('exp(-x^2)')
plt.grid(True, which='both')



#question 2
#question 2a
def f(t):
    return t**3-4*t**2+1
t=np.arange(-5,5,0.001)
plt.plot(t,f(t))
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid(True, which='both')
plt.ylim(-10,10)
plt.axvline(x = 0, color = "r")
plt.axhline(y = 0, color = "r")
#question 2b
coeff=[1,-4,0,1]
temparray=np.roots(coeff)
print("Roots are:")
for each in temparray:
    print(each)

#question2c
temp=sp.diff(x**3-4*x**2+1,x)

print(" for "+str(sp.reduce_abs_inequalities([(temp,'>=')],x))+" function is increasing")
print(" for "+str(sp.reduce_abs_inequalities([(temp,'<=')],x))+" function is decreasing")

a,b=sp.solveset(temp,x)
temp2=sp.diff(temp,x)
tempfunction=sp.utilities.lambdify(x,temp2)
if(tempfunction(a)>0):
    print("At point "+str(a)+" function is minimum")
elif(tempfunction(a)<0):
    print("At point "+str(a)+" function is maximum")
else:
    print("point "+str(a)+" is saddle point")
if(tempfunction(b)>0):
    print("At point "+str(b)+" function is minimum")
elif(tempfunction(b)<0):
    print("At point "+str(b)+" function is maximum")
else:
    print("point "+str(b)+" is saddle point")






#question 3
#question 3a
print(sp.limit(((x**2+3*x-4)/(x-1)),x,1))

#question 3b
print(sp.limit((sp.sin(x)/x),x,0))

#question 3c

print(sp.limit(x*sp.log(x),x,0,'+'))


#question 4
#question 4a
print(sp.diff((x**2+5*x-1)**100,x))
#question 4b 
print(sp.diff((sp.exp(x)*x**2-1)/(x**2+2),x))
#question 4c
print(sp.diff((sp.cos(x)**3)*(sp.sin(x)**5),x))

#question 4d
print(sp.diff(sp.atan(sp.exp(x)),x))

#question 5
#question 5a
print(sp.integrate(((2*x+5)*(x**2+5*x-1)**10),x))

#question 5b
def integrand(x):
    return np.sin(x**3)
ans,err= intg.quad(integrand,0,1)
print(ans)
#question 5c
def integrand2(x):
    return x**5*(1-x**2)**1.5
ans2,err2= intg.quad(integrand2,0,1)
print(ans2)
