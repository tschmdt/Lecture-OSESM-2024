import math

# function that returns the number of turbines that need to be installed for a desired capacity (input)
# a standard wind turbine with an output of 3 MW serves as the basis (Vestas V90 3 MW Onshore)
def number_of_turbines(installed_capacity):
    return math.ceil(installed_capacity / 3) # round up to the nearest whole number

# function that calculates the energy output for a wind farm over its lifetime with given wind density,
# rotor diameter, air density, efficency and lifetime
# varaiale parameters are installed_capacity, average_wind_speed and full_load_hours
# Units: installed_capacity in MW, average_wind_speed in m/s, full_load_hours in hours, lifetime in years, rotor_diameter in m,
# wind_density in kg/m^3, energy_output in TWh
# Base model turbine vestas V90 3 MW Onshore

wind_density = 1.225 # kg/m^3
rotor_diameter = 90 # m
efficiency = 0.40
lifetime = 20 # years


def energy_output(installed_capacity, average_wind_speed, full_load_hours):
    energy_output = (0.5 * wind_density * math.pi * (rotor_diameter/2)**2 * average_wind_speed**3 * efficiency * full_load_hours * math.ceil(installed_capacity/3) * lifetime)/ 1000/1000
    return round(energy_output/10**6,3) # convert to TWh









