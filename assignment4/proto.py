import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

tau = .0001
N = 61
L = 1
h = L/(N-1)

kappa = 1.
coeff = kappa*tau/h**2

tt = np.zeros(N)
#tt(np.round(N/2)) = 1/h

iplot = 1
nstep = 300
plot_step = 6
nplots = 51#nstep/plot_step + 1

tt = np.zeros(N)
tt[round(N/2)] = 1/h
tt_new = np.zeros(N)
xplot = np.zeros(N)
tplot = np.zeros(nplots)
ttplot = np.zeros((N, nplots))

for i in range(1, N):
    xplot[i] = (i-1)*h - L/2

for i in range(1, nstep):
    for n in range(2, N-1):
        tt_new[n] = tt[n] + coeff*(tt[n+1] + tt[n-1] - 2*tt[n])

    tt = tt_new

    if ( i%plot_step < 1):
        for k in range(1, N):
            ttplot[k, iplot] = tt[k]
        tplot[iplot] = i * tau
        iplot += 1

X = tplot
Y = xplot
X, Y = np.meshgrid(X, Y)
Z = ttplot

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

plt.show()