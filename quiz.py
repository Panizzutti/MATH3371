import numpy as np
n=5
A= np.array([[3,0,1],[-2,3,0],[1,2,3],[2,-4,3],[5,3,-2]])

a1=A[:,0]
n1=np.linalg.norm(a1)

w1= np.array([-n1,0,0,0,0])

print(w1)

v1=(a1-w1)
print("\nv1\n",v1)
v1=v1*(1/v1[0])
print("\nv1\n",v1)


tau=2/np.linalg.norm(v1)**2

print("\ntau\n",tau)

H1= np.identity(n)-tau*np.outer(v1,v1)

print(tau*np.outer(v1,v1))

print("\n H1 \n",H1)

print("\n H1@A \n",H1@A)

print("\n H1@A \n",np.ndarray.round(H1@A, 2))


print("\n\n",np.linalg.qr(A)[0])
print("\n\n",np.linalg.qr(A)[1])
