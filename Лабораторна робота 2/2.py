import numpy as np 
import matplotlib.pyplot as plt 
from scipy.misc import derivative

def f(x):
    return 4.5*pow(x,4) - 4*pow(x,3) + 1.5*pow(x,2) - 2*x - 7
a = 1.
b = 2.
eps = 0.0001 #точність

def hord(a, b, eps):
    if (f(a)*derivative(f, a, n = 2)>0):
        x0 = a
        xi = b
    else:
        x0 = b
        xi = a
    xi_1 = xi-(xi - x0) * f(xi)/(f(xi) - f(x0))
    while (abs(xi_1 - xi) > eps):
        xi = xi_1
        xi_1 - xi-(xi - x0) * f(xi)/(f(xi) - f(x0))
    print (f'Метод хорд.Корінь знаходиться в точці -', round(xi_1,5))
    return xi_1

hord(-5,-1,0.0001)
hord (4, 10, 0.0001)