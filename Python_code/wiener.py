# File wiener.py

""" An example of a Wieber process, or 1D Brownian motion
    From the book Python for Scientists
"""

import numpy as np
import numpy.random as npr

T=1   # time intercale of one secont
N = 500  # number of steps in the interval
t,dt=np.linspace(0,T,N+1,retstep=True)
dW=npr.normal(0.0,np.sqrt(dt),N+1)   # the delta W in the Brownian motion
dW[0]=0.0   # set initial position to 0
W=np.cumsum(dW)   # integrate the dW

import matplotlib.pyplot as plt
plt.ion()  # interactive plot mode

plt.plot(t,W)
plt.xlabel('t')
plt.ylabel('W(t)')
plt.title('Sample Wiener Process',weight='bold',size=16)
