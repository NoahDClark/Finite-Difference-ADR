import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

sizeX = 8
sizeY = 8
numX = 200
numY = 200
numT = 15000
maxTime = 250
K = 0.0053


dt = maxTime/(numT-1)
dx = sizeX/(numX-1)
dy = sizeY/(numY-1)

u = np.zeros((numT,numX,numY))
u[:,0,:] = u[:,numX-1,:] = u[:,:,0] = u[:,:,numY-1] = 0
u[:,95:105,95:105] = 5 
print(np.shape(u))
print(numT)

#Kronecker delta function
def tunc(gX, gY):
    if ((gX > 95) and (gX < 105)):
        if((gY > 95) and (gY < 105)):
            return 1.0
    return 0.0

for n in range(0,numT-1):
    u[n,0,:] = u[n,-2,:]
    for i in range(1,numX-1):
        for j in range(1,numY-1):
            u[n+1,i,j] = (u[n,i,j] 
                          - dt*(0.15*((u[n,i,j]-u[n,i-1,j])/dx) 
                                - K*( (u[n,i-1,j]-2*u[n,i,j]+u[n,i+1,j])/dx**2 + (u[n,i,j-1]-2*u[n,i,j]+u[n,i,j+1])/dy**2)
                                + u[n,i,j]*(1.1*10**(-4) + 1.7*10**(-4) + 3.3*10**(-5)) -5*(tunc(i,j))) )
            #end j
        #end i
    #tempVal = u[n,0,:]
    #u[n,-1,:] = tempVal
    if(n%10 == 0):
        print(n)
    #end n

test2 = u[14999,:,:]
plt.imshow(test2.T, extent=[0,8,0,8], cmap='viridis')
