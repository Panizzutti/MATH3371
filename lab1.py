import numpy as np



A= np.array([[2,0,1],[5,7,3],[-4,1,8],[9,4,6]])
print("A \n", A)

B= np.array([[1,1,2],[2,-1,6],[9,5,5]])
print("B \n", B)

x= np.array([[3,0,-5,2]]).T
print("x \n", x)


#####
print("AB \n", A@B)
    

print("ATx \n", A.T@x)
print("BAT \n", B@A.T)
print("ATA+B \n", A.T@A + B)
print("xTx-3 \n", x.T@x -3)

n=3

rng= np.random.default_rng()
A= rng.normal(size=(n,n))
B= rng.normal(size=(n,n))
C= rng.normal(size=(n,n))
a=3
b=-2
#3

res= a*A@B+b*C
print("actual result \n", res)

def GEMM(a,A,B,b,C):
    n=len(A)
    #print(n)
    R=np.zeros((n,n))

    for j in range(0,n):
        for i in range(0,n):
            s=0
            for k in range(0,n):
                s+=A[i,k]*B[k,j]
            R[i,j]= a*s+b*C[i,j]
            
    return R


M=GEMM(a,A,B,b,C)
print("my result \n",M)

print("my result - actual \n",M-res)

n=1
N=[]
times1=[]
times2=[]
from time import time

from threadpoolctl import threadpool_limits

while(True):

    rng= np.random.default_rng()
    A= rng.normal(size=(n,n))
    B= rng.normal(size=(n,n))
    C= rng.normal(size=(n,n))
    a=3
    b=-2
    
    start = time()
    D = a * (A @ B) + a * C
    #GEMM(a,A,B,b,C)
    elapsed_time = time() - start
    print("with ",n, "time=", elapsed_time)
    times1.append(elapsed_time)

    #####start = time()
    #####GEMM(a,A,B,b,C)
    #####elapsed_time = time() - start
    #####print("with ",n, "time=", elapsed_time)
    #####times2.append(elapsed_time)
    

    start = time()
    #GEMM(a,A,B,b,C)

    nt = 1 # if using only 1 thread
    with threadpool_limits(limits=nt, user_api='blas'):
        C = a * (A @ B) + b * C
    elapsed_time = time() - start

    print("with ",n, "time=", elapsed_time)
    times2.append(elapsed_time)



    N.append(n)
    #print("with ",n, "time=", elapsed_time)

    n+=2500
    if elapsed_time>10:
        break
    


for i in range(len(N)):
    print("n ", N[i], 't1=', times1[i],'t2= ', times2[i])


import matplotlib.pyplot as plt

plt.plot(N,times1)
plt.plot(N,times2)
plt.show()



nt = 1 # if using only 1 thread
with threadpool_limits(limits=nt, user_api='blas'):
    C = a * (A @ B) + b * C





#print(F)


#from threadpoolctl import threadpool_limits

#nt = 1 # if using only 1 thread
#with threadpool_limits(limits=nt, user_api='blas'):
    #C = alpha * (A @ B) + beta * C