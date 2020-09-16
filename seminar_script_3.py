import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


#Setting initial parameters
r=1
a=0.4
m=0.01
b=0.3

# function that returns dz/dt
def model(z,t):
	x=z[0]
	y=z[1]
	dxdt = r*x - a*x*y
	dydt = -m*y + b*x*y
	dzdt = [dxdt,dydt]
	return dzdt

# initial condition
z0 = [1/10,2/10]

# time points
t = np.linspace(0,10)

# solve ODE
z = odeint(model,z0,t)

# plot results
plt.plot(t,z[:,0],'b-',label=r'$\frac{dx}{dt}= r*\;x(t)\ -a*\;x(t)*\;y(t)$')
plt.plot(t,z[:,1],'r--',label=r'$\frac{dy}{dt}= -m*\;y(t)\ + b*\;x(t)*\;y(t)$')
plt.ylabel('response')
plt.xlabel('time')
plt.legend(loc='best')
plt.show()
