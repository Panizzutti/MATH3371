import numpy as np
from scipy.linalg import cho_factor, cho_solve, lu_factor
from time import time
from threadpoolctl import threadpool_limits
from scipy import linalg
from scipy.linalg import qr, solve_triangular, norm, inv



n=6
A=np.zeros((n,n))
#B=np.zeros((n,n))
#b=np.array([1,-1,1,-1,1])

for i in range(n):
    for j in range(n):
        A[i,j]=1+(1/(1+abs(i-j)))

print("\n\n A\n", A)

ei=linalg.eigh(A)

lmbda=ei[0]


V=ei[1]

print("\n\n giusto \n ",V@np.diag(lmbda)@V.T)
#print("\n\n ei val\n", ei[0])

#print("\n\n ei vec\n", ei[1])

#i
idx = np.argsort(-abs(lmbda))
lmbda = lmbda[idx]

print("\n\n lmbd\n", lmbda)

np.array(V)
print(idx)
V=V.T[idx].T
#V=V.T
print("\n\n ei vec\n", V)


np.savez

##ii
L=np.diag(lmbda)
print("\n\n LAMBDA\n", L)

print("\n\n A??\n", V@L@V.T)


#iii
print("\n\n A-V@L@V.T\n", A - V @ L @ V.T)



print("\n\n VTV-I \n", V@V.T-np.identity(n))

#iv
for i in range(n):

    print( "norm", norm(A@V.T[i]- lmbda[i]*V.T[i]) )


#2

outfile = "file.npz"
np.savez(outfile, lmbda=lmbda, V=V, A=A)


