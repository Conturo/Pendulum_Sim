import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib.animation import FuncAnimation

# Parameters
g = 9.81  # gravitational acceleration (m/s^2)
L = 1.0   # length of the pendulum (m)
theta0 = np.radians(45)  # initial angle (converted to radians)
omega0 = 0.0  # initial angular velocity (rad/s)

# System of equations
def pendulum_equations(y, t, L, g):
    theta, omega = y  # unpack theta and omega
    dydt = [omega, -(g/L) * np.sin(theta)]  # dtheta/dt = omega, domega/dt = -(g/L) * sin(theta)
    return dydt

# Time array and initial conditions
t = np.linspace(0, 5, 250)  # time from 0 to 10 seconds, 250 points
initial_conditions = [theta0, omega0]  # initial conditions

# Solve the differential equation
solution = odeint(pendulum_equations, initial_conditions, t, args=(L, g))
theta = solution[:, 0]  # extract the angle theta

# Convert theta to x and y coordinates of the pendulum bob
x = L * np.sin(theta)  # x = L * sin(theta)
y = -L * np.cos(theta)  # y = -L * cos(theta)

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-L-0.1, L+0.1)  # set the limits for x-axis
ax.set_ylim(-L-0.1, 0.1)    # set the limits for y-axis
ax.set_aspect('equal')       # make the aspect ratio equal
ax.grid(True)

# Create the pendulum rod and bob as plot objects
line, = ax.plot([], [], lw=2)  # pendulum rod (line)
bob, = ax.plot([], [], 'go', markersize=10)  # pendulum bob (point)

# Initialization function for the animation
def init():
    line.set_data([], [])
    bob.set_data([], [])
    return line, bob

# Animation function that updates the pendulum position
def update(i):
    # Update the rod
    line.set_data([0, x[i]], [0, y[i]])  # line goes from (0,0) to (x[i], y[i])
    # Update the bob (single points need to be sequences)
    bob.set_data([x[i]], [y[i]])  # pendulum bob at (x[i], y[i])
    return line, bob

# Create the animation
ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=40)

# Display the animation
plt.show()