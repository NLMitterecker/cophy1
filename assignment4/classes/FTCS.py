import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class FTCS:

    def __init__(self, ftcs_config):
        self.config = ftcs_config

    def calculate(self):

        for i in range(1, self.config.N):
            self.config.xplot[i] = (i - 1) * self.config.h - self.config.L / 2

        for i in range(1, self.config.nstep):
            for n in range(2, self.config.N - 1):
                self.config.tt_new[n] = self.config.tt[n] + self.config.coeff * (self.config.tt[n + 1] + self.config.tt[n - 1] - 2 * self.config.tt[n])

            self.config.tt = self.config.tt_new

            if (i % self.config.plot_step < 1):
                for k in range(1, self.config.N):
                    self.config.ttplot[k, self.config.iplots] = self.config.tt[k]
                self.config.tplot[self.config.iplots] = i * self.config.tau
                self.config.iplots += 1

    def draw_plot(self):

        X = self.config.tplot
        Y = self.config.xplot
        X, Y = np.meshgrid(X, Y)
        Z = self.config.ttplot
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
        plt.show()

