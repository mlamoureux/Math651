# File mandel.py
""" Code to draw the Mandelbrot set.
    from the book Python for Scientists.
    Uses numpy as well as the Python imaging library
"""

import numpy as np
from time import time

# set the parameters
max_iter = 256   # max number of interactions in the mandel repetition
nx,ny = 1024,1024 # number of cells (pixel) in x and y range
x_lo,x_hi = -2.0,1.0     # range for x values
y_lo,y_hi = -1.5,1.5    # range for y values
start_time = time()

# Construct the two dimentional arrayus
ix,iy = np.mgrid[0:nx,0:ny]  # integer indices
x,y = np.mgrid[x_lo:x_hi:1j*nx,y_lo:y_hi:1j*ny] # mesh grid. the complex number just means we include the right endpoints.
c = x+1j*y;
esc_parm=np.zeros((nx,ny,3),dtype='uint8') # pixel data in rgb format

# Flatten arrays, for speed
nxny=nx*ny;
ix_f=np.reshape(ix,nxny)
iy_f=np.reshape(iy,nxny)
c_f=np.reshape(c,nxny)
z_f=c_f.copy()

for ii in xrange(max_iter) :# do the iterations
    if not len(z_f):        # all the points have escapes
        break
    # rgb values for this choice of iterm
    n=ii+1;
    r,g,b=n%4*64,n%8*32,n%16*16
    # Mandelbrot evolution, in two computations
    z_f*=z_f
    z_f+=c_f
    escape=np.abs(z_f) > 2.0  # points which are escaping
    # Set the rgb pixel values for all the escaping points at once
    esc_parm[iy_f[escape],ix_f[escape],:]=r,g,b
    escape=-escape  # points not escaping (maybe 1-escape?)
    # this next little step keeps only the points of interest, for next stage
    ix_f=ix_f[escape]
    iy_f=iy_f[escape]
    c_f=c_f[escape]
    z_f=z_f[escape]
    
print "Time taken = ", time() - start_time

from PIL import Image

picture=Image.fromarray(esc_parm)
picture.show()
picture.save("mandelbrot.jpg")