"""
A two wheeled personal bike.
"""
# Imports
from .wheeled_vehicles import WheeledVehicles


# Motorcycle: Class definition
class Motorcycle(WheeledVehicles):

    def __init__(self, name, manufacturer, cc, fuel='Gasoline'):
        self.manufacturer = manufacturer
        self.cubiccapacity = cc
        super(Motorcycle, self).__init__(name=name, num_wheels=4, fuel=fuel)

    def summary(self):
        print("This bike named {} was manufactured by {}, "
              "with a {} cc engine that runs on {}.".format(self.name, self.manufacturer,
                                                            self.cubiccapacity, self.fuel))

