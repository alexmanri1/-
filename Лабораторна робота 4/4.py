import numpy as np
def N1():
    A=np.matrix([[1,2,],[4,-1,]])
    B=np.matrix([[2,-3,],[4,-1,]])
    rezult=A*B-B*A
    print(f"\n1\n{rezult}")

def N2():
    A=np.array([[-1,2,],[0,-1,]])
    rezult=A**2
    print(f"\n2\n{rezult}")

def N3():
    A=np.array([[3,5,],[6,-1,]])
    B=np.array([[2,1,],[-3,2,]])
    rezult=A*B
    print(f"\n3\n{rezult}")

def N4():
    A=np.matrix([[2,3,4,],[1,0,6,],[7,8,9,]])
    rezult=np.linalg.det(A)
    print(f"\n4\n{rezult}")

def N5():
    A=np.array([[1,2,3,4,],[-2,1,-4,3,],[3,-4,-1,2],[4,3,-2,-1]])
    rezult=np.linalg.det(A)
    print(f"\n5\n{rezult}")

def N6():
    A=np.array([[1,2,3,],[0,1,2,],[0,0,1,]])
    rezult=np.linalg.inv(A)
    print(f"\n6\n{rezult}")   

def N7():
    A=np.array([[1,2,3,4],[3,-1,2,5],[1,2,3,4],[1,3,4,5]])
    rezult=np.linalg.matrix_rank(A)
    print(f"\n7\n{rezult}") 

a=np.array([[14,4,6,],[5,3,2],[1,2,3,4],[10,11,5]])
b=np.array([[30],[15],[36]])
def kramer(a, b):
    a_det = np.linalg.det(a)
    print('Детермінант мфтриці = ', a_det)
    if (a_det !=0):
        print ('Розв*язуємо систему')
        x_m = np.matrix(a)
        x_m[:, 0] = b 
        print('x_m=', x_m)
        y_m = np.matrix(a)
        y_m[:, 1] = b
        print('y_m=', y_m)
        z_m = np.matrix(a)
        z_m[:, 2] = b
        print('z_m=', z_m)
        x = np.linigal.det(x_m) / a_det
        y = np.linigal.det(y_m) / a_det
        z = np.linigal.det(z_m) / a_det
        print('X =', round(x,5))
        print('y =', round(y,5))
        print('Z =', round(z,5))   
    else:
        print('Розв*язків немає')
kramer(a,b)

   


    
