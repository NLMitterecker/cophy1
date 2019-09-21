import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import g, pi

class BifurcationConfig:

    def __init__(self):
        self.omega = []
        self.theta = []
        self.dt = (2 * np.pi / (2.0 / 3.0)) / 600
        self.time = []
        self.theta_bifurcation = []
        self.FD = np.arange(1.35, 1.5, 0.001)
        self.theta_vs_FD = []
        self.l = 9.8
        self.q = 0.5
        self.Omega_D = 2/3

class Bifurcation:

    def __init__(self, bifurcation_config):
        self.config = bifurcation_config

    def calculate(self):

        for fd_step in self.config.FD:
            self.config.omega.append([0])
            self.config.theta.append([0.2])
            self.config.time.append([0])

            for i in range(500000):
                _omega = self.config.omega[-1][-1] - ((g / self.config.l) * np.sin(self.config.theta[-1][-1]) +
                                                      self.config.q * self.config.omega[-1][-1] - fd_step *
                                                      np.sin(self.config.Omega_D * self.config.time[-1][-1])) *\
                         self.config.dt
                _theta = self.config.theta[-1][-1] + _omega * self.config.dt

                while _theta > np.pi:
                    _theta -= 2 * pi
                while _theta < -np.pi:
                    _theta += 2 * pi

                self.config.omega[-1].append(_omega)
                self.config.theta[-1].append(_theta)
                self.config.time[-1].append(self.config.dt * i)

            for step in range(300, 700):
                n = step * 600
                self.config.theta_bifurcation.append(self.config.theta[-1][n])
                self.config.theta_vs_FD.append(fd_step)

    def draw_plot(self):

        plt.plot(self.theta_vs_FD, self.theta_bifurcation, '.')
        plt.title('Bifurcation')
        plt.xlabel(r'$F_D$')
        plt.ylabel(r'$\theta$ (radians)')
        plt.xlim(1.35, 1.5)
        plt.ylim(1, 3)
        plt.show()


bifurcation_config = BifurcationConfig()
bifurcation = Bifurcation(bifurcation_config)
bifurcation.calculate()
bifurcation.draw_plot()
