import math

# function that returns the number of turbines that need to be installed for a desired capacity (input)
# a standard wind turbine with an output of 3 MW serves as the basis (Vestas V90 3 MW Onshore)
def number_of_turbines(capacity):
    return math.ceil(capacity / 3) # round up to the nearest whole number






