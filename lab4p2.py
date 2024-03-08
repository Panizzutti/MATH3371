import numpy as np
from scipy.linalg import cho_factor, cho_solve, lu_factor
from time import time
from threadpoolctl import threadpool_limits


from scipy.linalg import cho_factor
from scipy.sparse import spdiags, csc_matrix, kron
from scipy.sparse.linalg import splu

n=5
A=np.zeros((n,n))
for i in range(n):
        for j in range(n):
            if i==j:
                A[i,j]=2
            elif abs(i-j)==1:
                A[i,j]=-1
            else:
                A[i,j]=0

print(A)

#B=kron(kron(A,I),I)+kron(kron(I,A),I)+kron(kron(I,I),A)

#print(B)

def sparse_poisson(n):

    A=np.zeros((n,n))
    I=np.identity(n)

    for i in range(n):
            for j in range(n):
                if i==j:
                    A[i,j]=2
                elif abs(i-j)==1:
                    A[i,j]=-1
                else:
                    A[i,j]=0

    K=kron(kron(A,I),I)+kron(kron(I,A),I)+kron(kron(I,I),A)

    return K


B = sparse_poisson(10)

print(B)

denseB = B.toarray()
print(denseB)

