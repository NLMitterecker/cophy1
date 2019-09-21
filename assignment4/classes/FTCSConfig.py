import numpy as np

class FTCSConfig:

    def __init__(self, tau, N, L, kappa, iplots, nstep, plot_step, nplots):
        self.tau = tau
        self.N = N
        self.L = L
        self.kappa = kappa
        self.h = self.L / (self.N - 1)
        self.coeff = self.kappa * self.tau/self.h**2
        self.tt = np.zeros(self.N)
        self.iplots = iplots
        self.nstep = nstep
        self.plot_step = plot_step
        self.nplots = nplots
        self.tt[round(N / 2)] = 1 / self.h
        self.xplot = np.zeros(self.N)
        self.tplot = np.zeros(self.nplots)
        self.ttplot = np.zeros((self.N, self.nplots))
        self.tt_new = np.zeros(self.N)