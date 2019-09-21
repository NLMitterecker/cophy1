import math
import numpy as np
from scipy.constants import g, pi
import matplotlib.pyplot as plt

class PendulumConfig:

    def __init__(self, dt, q, fd, th0,
                 dr, l, nmax, dth, dom):

        self.th0 = th0 *np.pi/180   # initial angle
        self.dt = dt                # time step
        self.q = q                  # damping constant
        self.fd = fd                # force amp
        self.l = l                  # pendulum length
        self.nmax = nmax
        self.dth = dth              # change angle
        self.dom = dom              # change angular velocity
        self.dr = dr                # frequency

class Pendulum:

    def __init__(self, pendulum_config):
        self.config = pendulum_config
        self.t = np.zeros(pendulum_config.nmax)
        self.th = np.zeros(pendulum_config.nmax)
        self.om = np.zeros(pendulum_config.nmax)
        self.th[0] = pendulum_config.th0
        self.om[0] = 0          # omega 0 ???
        self.theta_in_bifurcation_diagram = []
        self.theta_versus_F_D = []
        # th0 ... initial angle
        # om ... angular velocity
        # l ... pendulum length

    def calculate(self):
        # TODO bifurcation via decorator over calculate
        for f_d in np.arange(self.config.fd, self.config.fd+0.035, 0.001):
            for step in range(1, self.config.nmax):
                self.t[step] = self.t[step - 1] + self.config.dt
                self.config.dom = self.dv(
                        self.om[step-1],
                        self.th[step-1],
                        self.t[step-1],
                        g,
                        self.config.l,
                        self.config.q,
                        self.config.fd,
                        self.config.dr)

                self.om[step] = self.om[step - 1] + self.config.dt * self.config.dom
                self.th[step] = self.th[step - 1] + self.config.dt * self.om[step]
# If θi+1 is out of the range [-π,π], add or subtract 2π to keep it in this range
# read pseudocode description in slides!
                while self.th[step] > np.pi:
                    self.th[step] -= 2 * np.pi
                while self.th[step] < -np.pi:
                    self.th[step] += 2 * np.pi

            for step in range(500, 1000):
                n = step * 600
                self.theta_in_bifurcation_diagram.append(self.th[n])
                self.theta_versus_F_D.append(f_d)

    def dv(self, om0, th0, t0, g, l, q, fd, dr):
        return -g / l * math.sin(th0) - q * om0 + fd * math.sin(dr * t0)        # dr ... Omega_D

    def get_t(self):
        return self.t

    def get_th(self):
        return self.th

    def get_om(self):
        return self.om

pendulum_config = PendulumConfig(l = 9.8,           # pendulum length
                                 dt = 0.1,         # time steps
                                 q = 0.5,           # damping
                                 fd = 1.31,        # ???
                                 th0 = 5,  # initial angle
                                 dr = 2/3,          # Omega?!
                                 nmax = 600000,
                                 dth = 0,           # omega
                                 dom = 5)           # delta angular velocity

pendulum = Pendulum(pendulum_config)
pendulum.calculate()
#plt.plot(pendulum.get_t(), pendulum.get_th())

plt.show()
plt.plot(pendulum.theta_versus_F_D, pendulum.theta_in_bifurcation_diagram, '.')
plt.xlabel(r'$F_D$')
plt.ylabel(r'$\theta$ (radians)')
plt.xlim(1.33, 1.39)
plt.ylim(1, 2)
plt.show()
# Rescale angle ???????
# n=nmax