import numpy as np 
from scipy import optimize
from scipy.misc import deravitive
import math 
x0 = 0.538
y0 = -0.139
delta = 0.1

def f1(x):
    return math.sin(x=0.5)-1
def f2(y):
    return math.cos(y-2)

def iter(x,y,e):
    xn = x
    yn = y
    xn1 = f2(x)
    yn1 = f1(y)
    n = 1
    while ((abs(xn1-xn)>=e)&(abs(yn1-yn)>=e)):
        xn = xn1
        yn = yn1
        xn1 = f2(xn1)
        yn1 = f1(yn1)
        n+= 1
    print('Simple iteration:')
    print('x=', xn, '\ny=', yn, '\nThe amount ofiteration=', n)
iter(x0, y0, 0.001)

def f3(x):
    return math.sin(x[0]+0.5)-x[1]-1, math.cos(x[0]-2)+x[1]-0
s=optimize.root(f3,[0,0.], method='hybr')    
print('Chek',s.x)


    
