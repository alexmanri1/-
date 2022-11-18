import numpy as np 
import matplotlib.pyplot as plt 
from scipy.misc import derivative

def f(x):
    return 4.5*pow(x,4) - 4*pow(x,3) + 1,5*pow(x,2) - 2*x - 7
a=1.
a=2.
eps = 0.0001 #точність

def dihotom(a, b, eps):
    while (abs(a-b) > eps):
        if f(a)*f((a+b)/2)<0:
            b = (a+b)/2
        else:
            a = (a+b)/2

    print('Корінь рівняння x = ', round((a+b)/2,5))

dihotom(-5,-1,0.0001)#розв"язок для 1 відрівка 
dihotom(4,9,0.0001)#для 2 відрізк

x = np.arange(a, b, 0.01)

plt.plot (x, f(x))

plt.xlabel('x')

plt.ylabel('f(x)')

plt.title( "Метод ділення навпіл")

plt.grid()

plt. show()