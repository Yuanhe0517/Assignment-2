# main.py

import math

# Function for the population equation (rearranged to f(lambda) = 0)
def population_equation(lambda_value):
    left = 1564000
    right = 1000000 * math.exp(lambda_value) + (435000 / lambda_value) * (math.exp(lambda_value) - 1)
    return right - left

# Derivative of the function
def derivative_population_equation(lambda_value):
    exp_lambda = math.exp(lambda_value)
    term1 = 1000000 * exp_lambda
    term2 = 435000 * (exp_lambda - 1) / (lambda_value**2)
    term3 = 435000 * exp_lambda / lambda_value
    return term1 + term2 - term3

# Newton's method implementation
def newtons_method(initial_guess, tolerance=1e-4, max_iterations=100):
    lambda_value = initial_guess
    for iteration in range(max_iterations):
        f_lambda = population_equation(lambda_value)
        f_prime_lambda = derivative_population_equation(lambda_value)
        
        if abs(f_lambda) < tolerance:
            print(f"Converged to {lambda_value} in {iteration + 1} iterations")
            return lambda_value
        
        # Update lambda using Newton's method
        lambda_value -= f_lambda / f_prime_lambda
    
    print(f"Did not converge in {max_iterations} iterations")
    return lambda_value

if __name__ == "__main__":
    initial_guess = 0.1  # Initial guess for lambda
    lambda_value = newtons_method(initial_guess)
    print(f"Approximated lambda value: {lambda_value}")