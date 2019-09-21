import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class WaveSimulation:

    def __init__(self, wave_simulation_config):
        self.config = wave_simulation_config
        self.f, self.ax = plt.subplots()

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

    def animation_frame(self, step):
        self.ax = plt.axes(title='Waves on a string with fixed ends', xlim=(0, 0.001), ylim=(-2, 2))
        p, = self.ax.plot([], [], color='steelblue')
        X = self.config.x / self.config.string_dimension
        Y = self.config.simulation_data[step]
        p.set_data(X, Y[0])
        return p,

    def animate(self):
        gif = animation.FuncAnimation(self.f, self.animation_frame, interval=10, frames=10000, blit=True)
        plt.show()