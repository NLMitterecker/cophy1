import numpy as np

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