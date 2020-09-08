"""
This file demonstrates object oriented programming in Python
"""
# Imports
from oop_demo import personal_car, motorcycle, wheeled_vehicles

# Define an object
the_tesla = personal_car.PersonalCar(name="White Tesla", manufacturer="Tesla", model="Model S", fuel="Electric Power")

# And another
the_benz = personal_car.PersonalCar(name="Black Benz", manufacturer="Diamler AG", model="C180")

# Now the bike
the_bike = motorcycle.Motorcycle(name="Little Moped", manufacturer="Vespa", cc=35)

# See what we have
print("Summary: Car 1")
the_tesla.summary()

print("\nSummary: Car 2")
the_benz.summary()

print("\nSummary: Bike 1")
the_bike.summary()

# Use a function from the base class
print("\nThe name of Car 1 is {}".format(the_tesla.get_name()))

