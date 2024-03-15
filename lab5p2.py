
import numpy as np
from scipy.linalg import cho_factor, cho_solve, lu_factor
from time import time
from threadpoolctl import threadpool_limits
from scipy import linalg
from scipy.linalg import qr, solve_triangular, norm, inv

from scipy.stats import uniform_direction

D=np.load("file.npz")

lmbda = D['lmbda']
V= D['V']
A= D['A']
print(lmbda, V)
n= len(lmbda)


x0= uniform_direction.rvs(n)
print("\n",norm(x0),"\n random direction\n",x0)
l1=lmbda[0]
m=23
x=x0
print("x-v1 | -x-v1 | bk-l1 | -bk-l1   \n")
for i in range(m):

    y=A@x
    b=norm(y)

    print("step",i,": ", norm(x-V.T[0])," | ", norm(-x-V.T[0])," | ", b-l1," | ", -b-l1 )
    x=(1/b)*y




print("\neigen val:", b)
print("eigen vec:", x)


#3

x0= uniform_direction.rvs(n)

eigenlist=[]

print("\n",norm(x0),"\n random direction\n",x0)

l1=lmbda[0]
m=23
x=x0
print(" roba   \n")
for i in range(m):

    y=A@x
    b=norm(y)

    print("step",i,": ", norm(x-V.T[0])," | ", norm(-x-V.T[0])," | ", b-l1," | ", -b-l1 )
    x=(1/b)*y
    