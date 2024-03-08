import numpy as np
from scipy.linalg import qr, solve_triangular, norm, inv
from numpy import loadtxt
from numpy.polynomial import Polynomial as Poly

from scipy.sparse.linalg import lsqr

A= np.array([[-4,3,1],[2,9,5],[4,-1,6],[2,5,8],[0,-5,7],[1,8,2]])

b=np.array([-7,30,51,62,48,11])

#i
QR=qr(A)
Q=QR[0]
R=QR[1]
print("\nQ\n",Q)
print("\nR\n", R)
print("\nQR\n", Q@R)

print("\nA-QR\n", A-Q@R)

print("\nQTQ-I\n", Q.T@Q-np.identity(6))

#iv 
Q1= Q[:,0:3]
print(Q1)

S=(inv(A.T@A))@A.T@b
print("\nSol\n", S)

S= lsqr(A,b)

print("\nSol\n", S)

S= solve_triangular(R[0:3,:], Q1.T@b)

print("\nSol finale\n", S)

res=b- A@(inv(A.T@A))@A.T@b
print("\nRes\n", res)

print("\nResnorm\n", norm(res))

#2
d=loadtxt("/Users/giorgiopanizzutti/Library/Mobile Documents/com~apple~CloudDocs/UNIVERSITA/$MATH3371 NUMERICAL LINEAR ALGEBRA/Lab Class Instructions-20240226/xy_data.txt")

print(d)

x=d[:,0]
y=d[:,1]

#ii
x0=1

S= solve_triangular(R[0:3,:], Q1.T@b)

A= np.column_stack((x**0,x**1,x**2,x**3,x**4))

QR=qr(A)
Q=QR[0]
R=QR[1]
print("\nQ\n",Q)
print("\nR\n", R)
print("\nQR\n", Q@R)

for i in range(1,6):
    print("\n\nsol ", i," ", solve_triangular(R[0:i,0:i], Q[:,0:i].T @ y))

print(np.mean(y))

