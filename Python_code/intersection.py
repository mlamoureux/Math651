import numpy as np
import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import Symbol

def f1(x):
    return x**2
def f2(x):
    return 0.5*x+2.0

x = Symbol('x')
x1,x2 =  solve(f1(x)-f2(x))

y1 = f1(x1)
y2 = f1(x2)

plt.plot(x1,f1(x1),'ro',markersize=10)
plt.plot(x2,f1(x2),'ro',markersize=5)

plt.fill([x1,0,x2],[y1,0,y2],'green',alpha=0.6)

xr = np.linspace(-8,8,50)
y1r = f1(xr)
y2r = f2(xr)

plt.plot(xr,y1r,'k')
plt.plot(xr,y2r,'k')

xr = np.linspace(x2,x1,50)
y1r = f1(xr)
y2r = f2(xr)

plt.plot([xr,xr],[y1r,y2r],'red')

plt.xlim(-5,5)
plt.ylim(0,10)

plt.show()