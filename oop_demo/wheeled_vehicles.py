"""
Base class for wheeled vehicles.
Defines the base functions and variables that a vehicle class must implement.
"""
# Imports
from abc import ABCMeta, abstractmethod


# Class definition
class WheeledVehicles(object):
    """
    The base class for wheeled vehicles.
    """
    __metaclass__ = ABCMeta

    def __init__(self, name, num_wheels=4, fuel='gasoline'):
        """
        Set up local variables
        :param name: unique identifier for the vehicle class
        :param num_wheels: self explanatory
        :param fuel: what propels the vehicle
        """
        self.name = name
        self.num_wheels = num_wheels
        self.fuel = fuel

    # An abstract method is a function that every derived class must implement
    @abstractmethod
    def summary(self):
        """
        Print out a summary of the vehicle
        """

    # Getter method for returning the name of the vehicle.
    def get_name(self):
        """
        Getter/lookup method for the name string
        :return: string describing the name of the vehicle
        """
        return self.name
