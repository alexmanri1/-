import numpy as np
import math 
from scipy.misc import derivative

def f(x):
    return 4.5*pow(x,4) - 4*pow(x,3) + 1.5*pow(x,2) - 2*x - 7

def komb(a,b,eps):
    if (derivative(f, a, n = 1)*derivative(f, a, n =2)>0):
        a0 = 0
        b0 = 0
    else:
        a0 = b
        b0 = a
    ai = a0
    bi = b0
    while abs(ai-bi)>eps:
        ai_1 = ai - f(ai)*(bi - ai)/(f(bi) - f(ai))
        bi_1 = bi - f(bi)/derivative(f, bi, n = 1)
        ai_1 = ai_1
        bi_1 = bi_1
    x = (ai_1+bi_1)/2
    return print(f"\nSolving the equation by Newton*s method x = {round(x, 5)}\n")

komb(-2, -1/2, 0.0001)
