# File testito.py

""" We test the Ito calculus, using a process U = exp(-W/2), where 
    W(t) is a Wiener process. Ito suggest we should find <U>(t) = exp(t/8).
    So we plot a few simulations of U(t), take the average of 5000 of them,
    and compare to the expontial curve.
    From the book Python for Scientists
"""

import numpy as np
import numpy.random as npr

T=1
N=1000       # the number of steps in the time interval [0,T]
M=5000      # the number of trials to run, then average
t,dt=np.linspace(0,T,N+1,retstep=True)
dW=npr.normal(0.0,np.sqrt(dt),(M,N+1))
dW[ : ,0]=0.0               # initial position for all M trials is 0
W=np.cumsum(dW,axis=1)      # run the Wiener process M times, one for each row
U=np.exp(- 0.5*W)           #  U is a function of the random process
Umean=np.mean(U,axis=0)      # average over the M trials
Uexact=np.exp(t/8)          # the expected average value, as predicted by Ito

# Plot it
import matplotlib.pyplot as plt
plt.ion()

plt.plot(t,Umean,'b-', label="mean of %d paths" % M)
plt.plot(t,Uexact, 'r-',label="exact U")
for i in range(5):
    plt.plot(t,U[i, : ], '--')
    
plt.xlabel('t')
plt.ylabel('U')
plt.title('U= exp(-W(t)/2) for Wiener Process W(t)',
        weight='bold',size=16)
plt.legend(loc='best')

maxerr=np.max(np.abs(Umean-Uexact))
print "With %d paths and %d intervals the max error is %g" % (M,N,maxerr)
