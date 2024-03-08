import numpy as np
from scipy.linalg import cho_factor, cho_solve, lu_factor
from time import time
from threadpoolctl import threadpool_limits

n=5
A=np.zeros((n,n))
B=np.zeros((n,n))
b=np.array([1,-1,1,-1,1])

for i in range(n):
    for j in range(n):
        A[i,j]=1+(1/(1+(i-j)**2))

for i in range(n):
    for j in range(n):
        B[i,j]=1+(1/(1+(2*i-3*j)**2))

print("\n\n A\n", A)
print("\n\n B\n", B)

C=cho_factor(A)
print("\n\n C\n", C)

S=cho_solve(C,b)


print("\n\n S\n", S)

#with threadpool_limits(limits=nt, user_api='blas'): False
times=[]
print("\n\n EPSILON\n", max(b-A@S))

print("\n\n machine epsilon\n", np.finfo(float).eps)

for i in [500,1000,2000,4000,8000]:
    n=i
    A=np.zeros((n,n))
    B=np.zeros((n,n))

    for i in range(n):
        for j in range(n):
            A[i,j]=1+(1/(1+(i-j)**2))

    for i in range(n):
        for j in range(n):
            B[i,j]=1+(1/(1+(2*i-3*j)**2))   

    start = time()
    cho_factor(A)
    elapsed_time1 = time() - start   

    start = time()
    lu_factor(B)
    elapsed_time2 = time() - start

    times.append((elapsed_time1,elapsed_time2))

    print("\n", n)
    print("cholesky",elapsed_time1 , "\n lu","cholesky: ",elapsed_time2  )



import matplotlib.pyplot as plt

plt.plot(times)

plt.ylabel('some numbers')
plt.show()
    


#with threadpool_limits(limits=nt, user_api='blas'):

