# main.py

import math

# Given values
g = 32.17  # acceleration due to gravity in ft/s^2
m = 0.25  # mass of the object in lb
k = 0.1   # air resistance coefficient in lb-s/ft
s0 = 300  # initial height in ft
target_s = 0  # target height (ground level) in ft

# Define the height function s(t)
def height_function(t):
    return s0 - (m * g / k) * t + (m**2 * g / k**2) * (1 - math.exp(-k * t / m))

# Fixed-point iteration method
def fixed_point_iteration(f, target, low, high, tol=1e-5):
    t = (low + high) / 2.0  # initial guess
    while abs(f(t) - target) > tol:
        t = f(t)
    return t

# Rearranged function for fixed-point iteration
def rearranged_function(t):
    return (s0 - (m * g / k) * t + (m**2 * g / k**2) * (1 - math.exp(-k * t / m))) / (m * g / k)

# Function to find the time to hit the ground
def find_time_to_hit_ground():
    # Initial guess for t (lower and upper bounds)
    t_low = 0
    t_high = 100  # We start with an arbitrary upper bound for time

    # Find the time t that makes s(t) = 0 (i.e., when the object hits the ground)
    time_result = fixed_point_iteration(rearranged_function, target_s, t_low, t_high)
    return time_result

if __name__ == "__main__":
    time = find_time_to_hit_ground()
    print(f"The time it takes for the object to hit the ground is approximately {time:.4f} seconds.")
