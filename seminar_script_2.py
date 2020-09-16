import numpy
import matplotlib.pyplot as plt


# set the initial parameters
alpha = 1.
beta = 1.2
gamma = 4.
delta = 1.

 

#define the time stepping scheme - euler forward, as used in earlier lessons
def euler_step(u, f, dt):
    
    return u + dt * f(u)


# define the function that represents the Prey Predator Model equations
def f(u):
    x = u[0]
    y = u[1]
    return numpy.array([x*(alpha - beta*y), -y*(gamma - delta*x)])

# set time-increment and discretize the time
T  = 15.0                           # final time
dt = 0.01                           # set time-increment
N  = int(T/dt) + 1                  # number of time-steps
x0 = 10.
y0 = 2.
t0 = 0.

# set initial conditions
u_euler = numpy.empty((N, 2))

# initialize the array containing the solution for each time-step
u_euler[0] = numpy.array([x0, y0])

# use a for loop to call the function rk2_step()
for n in range(N-1):
    
    u_euler[n+1] = euler_step(u_euler[n], f, dt)

time = numpy.linspace(0.0, T,N)
x_euler = u_euler[:,0]
y_euler = u_euler[:,1]

plt.plot(time, x_euler, label = 'Hare')
plt.plot(time, y_euler, label = 'Lynx')
plt.legend(loc='upper right')
#labels
plt.xlabel("time")
plt.ylabel("number of each species")
#title
plt.title("Prey-Predator model")
plt.show()
