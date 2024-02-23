#i

import numpy as np
A= np.array([[3,-5,1,0],[-2,9,3,3],[5,8,4,-6],[3,0,5,7]])

from scipy.linalg import toeplitz, inv, lu_factor, lu_solve
import scipy

PLU= scipy.linalg.lu(A)

print(PLU)