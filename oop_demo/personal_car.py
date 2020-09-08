"""
A four wheeled personal (non-commercial) vehicle.
"""
# Imports
from .wheeled_vehicles import WheeledVehicles


# Personal Car: Class definition
class PersonalCar(WheeledVehicles):

    def __init__(self, name, manufacturer, model, fuel='Gasoline'):
        self.manufacturer = manufacturer
        self.model = model
        super(PersonalCar, self).__init__(name=name, num_wheels=4, fuel=fuel)

    def summary(self):
        print(
            "This is a {}, which a {}-wheeled vehicle that runs on {}. It was manufactured by {}, "
            "with the model designation {}".format(
                self.name, self.num_wheels, self.fuel, self.manufacturer, self.model))
