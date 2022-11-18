import numpy as np
import math 
from scipy.misc import derivative

def f(x):
    return 4.5*pow(x,4) - 4*pow(x,3) + 1.5*pow(x,2) - 2*x - 7

def nuton(a,b,eps):
    df2 = derivative(f, b, n=1)
    if (f(b)*df2>0):
        xi = b
    else:
        xi = a
    df = derivative(f, xi, n=1)
    xi_1 = xi = f(xi)/df
    while (abs(xi_1 - xi)>eps):
        xi = xi_1
        xi_1 = xi - f(xi)/df
    return print(f"\nSolving the equation by Newton*s method x = {round(xi_1, 5)}\n")

nuton(-2, -1/2, 0.0001)