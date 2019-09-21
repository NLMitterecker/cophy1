import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class WaveSimulationConfig:

    def __init__(self, string_dimension, k, x_init, r):
        self.string_dimension = string_dimension
        self.x = np.linspace(1 / string_dimension, 1, num = string_dimension)
        self.y_dimension = np.zeros(string_dimension)
        self.x_init = x_init
        self.k = k
        self.initial_position = np.exp(-1 * self.k * (self.x - x_init)**2)
        self.y_current = self.initial_position
        self.y_previous = self.initial_position
        self.y_next = np.zeros(string_dimension)
        self.r = r
        self.simulation_data = []

class WaveSimulation:

    def __init__(self, wave_simulation_config):
        self.config = wave_simulation_config

    def reset_y_axis(self):
        self.config.y_next = np.zeros(self.config.string_dimension)

    def propagate(self):
        self.reset_y_axis()
        for step in range(2, self.config.string_dimension-1):
            self.config.y_next[step] = 2 * (1 - self.config.r**2) * self.config.y_current[step] - \
                                       self.config.y_previous[step] + (self.config.r**2) * \
                                       (self.config.y_current[step+1] + self.config.y_current[step-1])
        self.config.simulation_data.append([self.config.y_next])
        self.config.y_previous = self.config.y_current
        self.config.y_current = self.config.y_next

    def simulate(self, nmax):
        for steps in range(1, nmax):
            self.propagate()


simulation_config = WaveSimulationConfig(1000, 1000, 0.5, 1)
wave_simulation = WaveSimulation(simulation_config)
wave_simulation.simulate(1000)


#for step in range(1, simulation_config.string_dimension):
#    X = simulation_config.x / simulation_config.string_dimension
#    Y = simulation_config.simulation_data[step]
#    plt.plot(X, Y[0])
#    plt.show()

f, ax = plt.subplots()

def animate(step):
    ax = plt.axes(title='Waves on a string\n(fixed ends)', xlim=(0, 0.1), ylim=(-2, 2), xlabel='x (m)', ylabel='y (m)')
    p, = ax.plot([], [])
    X = (simulation_config.x / simulation_config.string_dimension)* 100
    Y = simulation_config.simulation_data[step]
    p.set_data(X, Y[0])
    return p,

gif = animation.FuncAnimation(f, animate, interval=simulation_config.string_dimension, frames=25, blit=True)
plt.show()

