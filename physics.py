import numpy as np
import math
from matplotlib import pyplot as plt
from matplotlib import rc
rc('font',**{'family':'serif','serif':['Times']})
rc('text', usetex=True)


# constants

m_mu = 105.658e-3 # Gev/c^2
t_mu = 2.2e-6 # s

N_mu = 2e12 # mu per bunch
duty_factor = 5e7 # injections/year
c = 3e8 #m/s

mass_diff_21 = 7.537e-5 # eV^2
mass_diff_31 = 2.521e-3 # eV^2

n_samples = 500

# functions

def gamma(E_mu):
    return (E_mu / m_mu)

def beta(E_mu):
    return (np.sqrt(1 - ((1 / (E_mu / m_mu)))**2))

def angular_dist(theta, gamma, beta):
    return ( (np.sin(theta)) / ( 2 * (gamma**2) * ((1 - beta*np.cos(theta))**2) ))

def integrated_angular_dist(theta0, theta1, gamma, beta):
    return (-1 / ( 2 * gamma**2 * beta )) * ( (1 / (1 - beta*np.cos(theta1))) - (1 / (1 - beta*np.cos(theta0))))

def prob_of_oscillation(mass_diff, E, L):
    p = np.sin( ((mass_diff * (L / 1000)) / (E)) * 1.27 )**2
    # L is given in m, and converted to km here
    return p


# the beginnings of a lattice library
# https://arxiv.org/pdf/2407.12450
# ^ pg. 76 , and 
# https://indico.cern.ch/event/1313021/contributions/5623393/attachments/2744752/4775555/IMCC_parameters_EU.pdf 
# ^ pg. 12

'''
E_0 is injection energy
E_f is ejection energy
'''

PA = {'name': 'PA', 'E_0': 0.255, 'E_f': 1.25, 'n_turns': 1, 'E_per_pass': 0.955, 'length': 0, 'color': 'tab:blue'}

RLA1 = {'name': 'RLA1', 'E_0': 1.25, 'E_f': 5, 'n_turns': 5, 'E_per_pass': 0.8, 'length': 0, 'color': 'green'}

RLA2 = {'name': 'RLA2', 'E_0': 5, 'E_f': 62.5, 'n_turns': 5, 'E_per_pass': 11.6, 'length': 0.955, 'color': 'c'}

RCS1 = {'name': 'RCS1', 'E_0': 63, 'E_f': 314, 'n_turns': 5, 'E_per_pass': 0, 'length': 5.99, 'color': 'tab:purple'}

RCS2 = {'name': 'RCS2', 'E_0': 314, 'E_f': 750, 'n_turns': 5, 'E_per_pass': 0, 'length': 5.99, 'color': 'red'}

RCS3 = {'name': 'RCS3', 'E_0': 750, 'E_f': 1500, 'n_turns': 5, 'E_per_pass': 0, 'length': 10.7, 'color': 'y'}

RCS4 = {'name': 'RCS4', 'E_0': 1500, 'E_f': 5000, 'n_turns': 5, 'E_per_pass': 0, 'length': 35, 'color': 'tab:orange'}

sections = [PA, RLA1, RLA2, RCS1, RCS2, RCS3, RCS4]

list_of_colors = ['tab:blue', 'green', 'c', 'tab:purple', 'red', 'y', 'tab:orange']

# ^ E in GeV

# E per pass for RCS sections are approximate/ average
# L for low-energy sections are unknown...?