# test function for the "numbers_of_turbines" function
# since the model turbine has an output of 3 MW, an installed capacity below 3 MW should still return 1 turbine

def test_number_of_turbines():
    assert number_of_turbines(1) == 1
    assert number_of_turbines(2) == 1
    assert number_of_turbines(3) == 1
    assert number_of_turbines(5) == 2
    assert number_of_turbines(100) == 34

