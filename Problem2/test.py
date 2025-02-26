# test_main.py

import main

def test_find_rate_of_change():
    # Test the find_rate_of_change function from main.py
    result = main.find_rate_of_change()
    print(f"Test result: The rate of change of theta (omega) is approximately {result:.5f} radians per second.")
    assert abs(result - 1.4852) < 1e-4, f"Test failed! Expected ~1.4852, but got {result}"

if __name__ == "__main__":
    test_find_rate_of_change()