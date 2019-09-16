import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class WaveSimulation:

    def __init__(self, SimulationConfig):
        self.simulation_config = SimulationConfig
        self.ycurrent = None
        self.yprevious = None
        self.ynext = None
        self.fig = plt.figure()
        self.ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
        self.line, = self.ax.plot([], [], lw=2)
        self.anim = None

    def initial_position(self):
        return np.exp(-1 * self.simulation_config.k() *
                      (self.simulation_config.segment_length()
                       - self.simulation_config.initial_position())**2)

    def set_ycurrent(self, position):
        self.ycurrent = position

    def set_yprevious(self, position):
        self.yprevious = position

    def init(self):
        self.line.set_data([], [])
        return self.line,

    def run(self, i):
        x = np.linspace(0, 2, 1000)
        y = np.sin(2 * np.pi * (x - 0.01 * i))
        self.line.set_data(x, y)
        return self.line,

    def draw(self):
        self.anim = animation.FuncAnimation(self.fig, self.run, init_func=self.init,
                                            frames=200, interval=20, blit=True)
        plt.show()



