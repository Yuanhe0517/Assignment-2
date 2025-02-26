import math
from main import population_equation, derivative_population_equation, newtons_method

def test_population_equation():
    # Test for the function population_equation
    lambda_value = 0.1  # Sample lambda value
    result = population_equation(lambda_value)
    assert abs(result - (1564000 - (1000000 * math.exp(lambda_value) + (435000 / lambda_value) * (math.exp(lambda_value) - 1)))) < 1e-6, "Test failed"
    print("Test for population_equation passed")

def test_derivative_population_equation():
    # Test for the derivative population_equation
    lambda_value = 0.1  # Sample lambda value
    result = derivative_population_equation(lambda_value)
    expected = 1000000 * math.exp(lambda_value) + 435000 * (math.exp(lambda_value) - 1) / (lambda_value**2) - 435000 * math.exp(lambda_value) / lambda_value
    assert abs(result - expected) < 1e-6, "Test failed"
    print("Test for derivative_population_equation passed")

def test_newtons_method():
    # Test for Newton's method
    initial_guess = 0.1
    lambda_value = newtons_method(initial_guess)
    assert abs(population_equation(lambda_value)) < 1e-4, "Test failed"
    print("Test for newtons_method passed")

if __name__ == "__main__":
    test_population_equation()
    test_derivative_population_equation()
    test_newtons_method()