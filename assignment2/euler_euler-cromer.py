import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.constants import g

class PendulumConfig:

    def __init__(self, init_theta, init_omega, time_resolution, pendulum_length, max_steps, pendulum_mass):
        self.init_theta = init_theta
        self.init_omega = init_omega
        self.time_resolution = time_resolution
        self.pendulum_length = pendulum_length
        self.max_steps = max_steps
        self.pendulum_mass = pendulum_mass

class Pendulum:

    def __init__(self, pendulum_config):
        self.config = pendulum_config
        self.time_vec = np.zeros(self.config.max_steps)
        self.theta_vec = np.zeros(self.config.max_steps)
        self.omega_vec = np.zeros(self.config.max_steps)
        self.total_energy = np.zeros(self.config.max_steps)
        self.kinetic_energy = np.zeros(self.config.max_steps)
        self.potential_energy = np.zeros(self.config.max_steps)
        self.theta_vec[0] = self.config.init_theta
        self.omega_vec[0] = self.config.init_omega
        self.kinetic_energy[0] = 0.5 * self.config.pendulum_mass * self.config.pendulum_length ** 2 * \
                                                                                            self.omega_vec[0] ** 2
        self.potential_energy[0] = 0.5 * self.config.pendulum_mass * self.config.pendulum_length**2 *\
                                                                                            self.omega_vec[0] ** 2
        self.total_energy[0] = self.kinetic_energy[0] + self.potential_energy[0]

        #self.total_energy[0] = 0.5 * self.config.pendulum_mass * self.config.pendulum_length**2 *\
        #                       self.omega_vec[0]**2 + self.config.pendulum_mass * g * self.config.pendulum_length *\
        #                       (1 - np.cos(self.theta_vec[0]))
    def euler_method(self):

        for step in range(1, self.config.max_steps):
            omega_old = self.omega_vec[step-1]
            theta_old = self.theta_vec[step-1]
            omega = omega_old - (g / self.config.pendulum_length) * np.sin(theta_old) * self.config.time_resolution
            theta = theta_old + omega_old * self.config.time_resolution
            self.total_energy[step] = self.total_energy[step-1] + 0.5 * self.config.pendulum_mass *\
                                      self.config.pendulum_length**2 * \
                                      ((omega**2 + g / self.config.pendulum_length) * theta**2) *\
                                      self.config.time_resolution
            self.time_vec[step] = self.config.time_resolution * step
            self.theta_vec[step] = theta
            self.omega_vec[step] = omega

    def euler_cromer_method(self):

        for step in range(1, self.config.max_steps):
            omega_old = self.omega_vec[step-1]
            theta_old = self.theta_vec[step-1]
            omega = omega_old - (g / self.config.pendulum_length) * np.sin(theta_old) * self.config.time_resolution
            theta = theta_old + omega * self.config.time_resolution
            self.kinetic_energy[step] = 0.5 * self.config.pendulum_mass * self.config.pendulum_length**2 * omega**2
            self.potential_energy[step] = self.config.pendulum_mass * g * self.config.pendulum_length * (1 - np.cos(theta))
            self.total_energy[step] = self.kinetic_energy[step-1] + self.potential_energy[step-1]
            self.time_vec[step] = self.config.time_resolution * step
            self.theta_vec[step] = theta
            self.omega_vec[step] = omega


    def draw_plot(self, type, confirm_save='', show_plot=False):
        plt.figure(0)
        if type == 'oscillation':
            plt.plot(self.time_vec, self.theta_vec)
            plt.xlabel('Time[s]')
            plt.ylabel('Velocity[rad/s]')
        elif type == 'energy':
            plt.plot(self.time_vec, self.kinetic_energy, label='Kinetic-Energy')
            plt.plot(self.time_vec, self.potential_energy, label='Potential-Energy')
            plt.plot(self.time_vec, self.total_energy, label='Total-Energy')
            plt.xlabel('Time[s]')
            plt.ylabel('Energy[J]')
            plt.legend(loc='lower right')

            if confirm_save != '':
                script_path = os.path.dirname(os.path.abspath(__file__))
                plt.savefig(os.path.join(script_path, confirm_save))
        else:
            raise Exception("Plot type not valid. Valid types: 'oscillation', 'energy'.")

        if show_plot:
            plt.show()

#theta0, omega0, tau, g, l, numSteps
pendulum_config = PendulumConfig(0.15, 0, 0.01, 9.8, 10000, 30)
pendulum = Pendulum(pendulum_config)

pendulum.euler_method()
#pendulum.euler_cromer_method()

#pendulum.draw_plot('energy', 'euler_cromer.png')
pendulum.draw_plot('energy', 'euler.png')

# Inputs: theta0 (the initial angle, in rad)
#		  omega0 (the initial angular velocity, in rad/s)
#		  tau (the time step)
#		  m (mass of the pendulum)
#	      g (gravitational constant)
#		  l (length of the pendulum)
#		  numSteps (number of time steps to take, in s)
