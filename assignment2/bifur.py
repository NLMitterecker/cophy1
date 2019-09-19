import math
import numpy as np
from scipy.constants import g

class PendulumConfig:

    def __init__(self, th, om, tl, dt, q, fd, dr, n, l,
                 period, nmax, t, om0, t0, th0, dth, dom):

        self.th = th
        self.om = om
        self.tl = tl
        self.dt = dt
        self.q = q
        self.fd = fd
        self.fd = dr
        self.n = n
        self.l = l
        self.period = period
        self.nmax = nmax
        self.t = t
        self.om0 = om0
        self.t0 = t0
        self.th0 = th0
        self.dth = dth
        self.dom = dom


class Pendulum:

    def __init__(self, pendulum_config):
        self.config = PendulumConfig
        pass

    def calculate(self):
        for step in range(2, self.config.nmax):
            self.config.t[step] = self.config.t[step - 1] + self.config.dt
            self.dv(self.config.om[step - 1], self.config.th[step - 1], self.config.t[step - 1], self.config.g,
                    self.config.l, self.config.q, self.config.fd, self.config.dr, self.config.dom, self.config.dth)
            self.config.om[step] = self.config.om[step - 1] + self.config.dt * self.config.dom
            self.config.th[step] = self.config.th[step - 1] + self.config.dt * self.config.om[step]

    def dv(self, om0, th0, t0, g, l, q, fd, dr):
        # returns dom!
        return -g / l * math.sin(th0) - q * om0 + fd * math.sin(dr * t0)

pendulum_config = PendulumConfig(l = 4,
                                 period = 6.2831853/(math.sqrt(g / 4)),
                                 th = 0,
                                 om = np.zeros(5003),
                                 tl = 0,
                                 dt = 0.2,
                                 q = 0,
                                 fd = 0,
                                 dr = 0,
                                 n = 0,
                                 nmax = 5003,
                                 t = np.zeros(5003),
                                 om0 = 0,
                                 t0 = 0,
                                 th0 = np.zeros(5003),
                                 dth = 0,
                                 dom = 0)

pendulum = Pendulum(pendulum_config)








# n=nmax