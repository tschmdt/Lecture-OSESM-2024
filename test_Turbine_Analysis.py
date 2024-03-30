from Turbine_Analysis import number_of_turbines, energy_output

# test function for the "numbers_of_turbines" function
# since the model turbine has an output of 3 MW, an installed capacity below 3 MW should still return 1 turbine

def test_number_of_turbines():
    assert number_of_turbines(1) == 1
    assert number_of_turbines(2) == 1
    assert number_of_turbines(3) == 1
    assert number_of_turbines(5) == 2
    assert number_of_turbines(100) == 34


# test function for the "energy_output" function
# Unit: TWh
def test_energy_output():
    assert energy_output(3, 6, 2500) == 0.017
    assert energy_output(1, 6, 2000) == 0.013
    assert energy_output(100, 6, 2500) == 0.572
    assert energy_output(250, 9, 2400) == 4.581
    assert energy_output(600, 6, 2000) == 2.693
