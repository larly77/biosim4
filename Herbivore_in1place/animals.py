# -*- coding: utf-8 -*-

"""
"""

__author__ = 'Jon-Fredrik Blakstad Cappelen', 'Lars Martin Boe Lied'
__email__ = 'jon-fredrik.blakstad.cappelen@nmbu.no',\
            'lars.martin.boe.lied@nmbu.no'


import random
import math


DEFAULT_HERBIVORE_PARAMETERS = {'w_birth': 8.0,
                           'sigma_birth': 1.5,
                           'beta': 0.9,
                           'eta': 0.05,
                           'a_half': 40.0,
                           'phi_age': 0.2,
                           'w_half': 10.0,
                           'phi_weight': 0.1,
                           'mu': 0.25,
                           'lambda': 1.0,
                           'gamma': 0.2,
                           'zeta': 3.5,
                           'xi': 1.2,
                           'omega': 0.4,
                           'F': 10.0}


class Herbivore:
    """"""

    def __init__(self, age, weight, parameters=None):
        self.parameters = parameters if parameters is not None \
                          else DEFAULT_HERBIVORE_PARAMETERS
        self.parameters['age'] = age
        self.parameters['weight'] = weight
        self.parameters['fitness'] = None
        self.update_fitness()

    def set_parameters(self, dictionary_changes):
        """Method that allows the user to set parameter values for the animal.
        This replaces the default values."""
#       Idiotsikring her?
        for key in dictionary_changes:
            self.parameters[key] = dictionary_changes[key]

    def update_fitness(self):
        """Method to update the fitness of the animal"""
        q_plus = 1/(1+math.exp(self.parameters['phi_age'] *
                            (self.parameters['age']-self.parameters['a_half'])))
        q_minus = 1/(1+math.exp(-self.parameters['phi_weight'] *
                         (self.parameters['weight']-self.parameters['w_half'])))

        self.parameters['fitness'] = q_plus * q_minus

    def feeding(self):
        """Dummy"""

    def procreation(self):
        """Dummy"""

    def migration(self):
        """Dummy"""

    def aging(self):
        """Method that increases the age of the animal by one year"""
        self.parameters['age'] += 1
        self.update_fitness()

    def loss_of_weight(self):
        """Method that decreases the weight of the animal by a percent-value"""
        self.parameters['weight'] -= self.parameters['eta'] *\
                                     self.parameters['weight']
        self.update_fitness()

    def death(self):
        """Dummy"""

#        probability_of_death = self.parameters['omega']*(1-fitness)


# Følgende angir hvordan en docstring bør se ut.
# Med det formatet blir dokumentasjons-porsessen meget grei,
# når vi lærer Sphinx-programmet.
def f(x):
    """
    one line description

    many line description

    Parameters
    ----------
    x : float
        Description of x

    Returns
    -------
    y : float
        The bladibla

    Raises
    ------
    ValueError
        If x is not numeric
    """
