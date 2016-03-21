import random #for the random entries in the matrix
import numpy as np 
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from numpy import linalg as LA# Linear Algebra package
matrix= np.random.rand(100,100) #Random 100x100 matrix
matrix_transpose= matrix.transpose()# Transpose is an in-built function
sym_matrix= np.dot(matrix, matrix_transpose)# matrix products are built in.
w,v= LA.eigh(sym_matrix) #w represents the eigenvalues while v is an array of the eigen vectors in the order in which they appear in w
print("Largest eigenvalue:", max(w))
print("Smallest eigenvalue:", min(w))
plt.hist(w,bins=1000) # histogram with 1000 bins
plt.xlim(-10,40)  # eigenvalues between -10 and 100
plt.xlabel('Eigenvalues')
plt.ylabel('Frequency')
plt.show()
