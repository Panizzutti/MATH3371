#i

import numpy as np
A= np.array([[3,-5,1,0],[-2,9,3,3],[5,8,4,-6],[3,0,5,7]])
b= np.array([-30,26,-19,-17]).T

from scipy.linalg import toeplitz, inv, lu_factor, lu_solve
import scipy

PLU= scipy.linalg.lu(A)

P=PLU[0].T
L=PLU[1]
U=PLU[2]
print(PLU[0])
print(PLU[1])
print(PLU[2])

#ii

print("\n\nA\n",A)

print("\n\nPA\n",P@A)

#iii
print("\n\nPA-LU\n",P@A-L@U)

#iv

pb=P@b

c=scipy.linalg.solve_triangular(L, pb, lower=True, unit_diagonal=True)
print("\n\nc\n",c)

x=scipy.linalg.solve_triangular(U, c, lower=False, unit_diagonal=False)
print("\n\nx\n",x)

print("\n\nA@x\n",A@x)


print("\n\nb-A@x\n",b-A@x)


d=np.array([-1, 4, -7, 3])
print("\n\nA@d\n",A@d)



####################2

n=4

A=np.zeros((n,n))

for i in range(n):
    for j in range(n):
        A[i,j]=3+(1/(2+abs(i-j)))

print("\n\nA\n",A)


v=np.zeros(n)

for i in range(n):
    v[i]= -1**(i+1)


#toeplitz()

#
#print("\n\nA\n",lu_factor(A))

#toeplitz()


from time import time

start = time()
J=inv(A)
elapsed_time = time() - start
print("\ntime=",elapsed_time)

start = time()
J=inv(A)@v
elapsed_time = time() - start
print("\ntime2=",elapsed_time)


start = time()
PLU= scipy.linalg.lu(A)
elapsed_time = time() - start
print("\ntime3=",elapsed_time)



