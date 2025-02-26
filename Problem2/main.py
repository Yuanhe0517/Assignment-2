# main.py

import math

# Given values
L = 10  # length of the trough in feet
r = 1   # radius of the semicircle in feet
V_target = 12.4  # target volume in cubic feet

# Define the volume function
def volume(h):
    return L * (0.5 * math.pi * r**2 - r**2 * math.asin(h/r) - h * (r**2 - h**2)**0.5)

# Bisection method to find the root
def bisection_method(f, target, low, high, tol=1e-5):
    # f is the function, target is the volume we are looking for
    # low and high are the initial bounds for h
    # tol is the tolerance for stopping the iteration
    while (high - low) / 2.0 > tol:
        mid = (low + high) / 2.0
        if f(mid) < target:
            low = mid
        else:
            high = mid
    return (low + high) / 2.0

# Initial guess for h
h_low = 0
h_high = r  # Maximum height of the water is the radius of the semicircle

# Find the depth of water (h) that gives the target volume
h_result = bisection_method(volume, V_target, h_low, h_high)

print(f"The depth of water in the trough is approximately {h_result:.4f} feet.")