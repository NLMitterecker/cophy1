import math
import numpy as np
from scipy.constants import g

class PendulumConfig:

    def __init__(self, tl, dt, q, fd, dr, n, l,
                 period, nmax, om0, t0, th0, dth, dom):

        self.tl = tl
        self.dt = dt
        self.q = q
        self.fd = fd
        self.n = n
        self.l = l
        self.period = period
        self.nmax = nmax
#        self.om0 = om0
#        self.t0 = t0
#        self.th0 = th0
        self.dth = dth
        self.dom = dom
        self.dr = dr

class Pendulum:

    def __init__(self, pendulum_config):
        self.config = pendulum_config
        self.t = np.zeros(pendulum_config.nmax)
        self.th = np.zeros(pendulum_config.nmax)
        self.om = np.zeros(pendulum_config.nmax)

    def calculate(self):
        for step in range(2, self.config.nmax):
            self.t[step] = self.t[step - 1] + self.config.dt
            self.dv(self.om[step - 1],
                    self.th[0],
                    self.t[0],
                    g,
                    self.config.l,
                    self.config.q,
                    self.config.fd,
                    self.config.dr)

            self.om[step] = self.om[step - 1] + self.config.dt * self.config.dom
            self.th[step] = self.th[step - 1] + self.config.dt * self.om[step]

    def dv(self, om0, th0, t0, g, l, q, fd, dr):
        # returns dom!
        return -g / l * math.sin(th0) - q * om0 + fd * math.sin(dr * t0)

    def get_t(self):
        return self.t

    def get_th(self):
        return self.th

    def get_om(self):
        return self.om
pendulum_config = PendulumConfig(l = 9.8,
                                 period = 6.2831853/(math.sqrt(g / 4)),
                                 om0 = 0,
                                 th0 = 0.2,
                                 tl = 0,
                                 dt = 0.01,
                                 q = 0.5,
                                 fd = 0,
                                 dr = 0,
                                 n = 0,
                                 nmax = 5003,
                                 t0 = 0,
                                 dth = 0,
                                 dom = 0)

pendulum = Pendulum(pendulum_config)
pendulum.calculate()
print(pendulum.get_om())
print(pendulum.get_th())
print(pendulum.get_t())






# n=nmax