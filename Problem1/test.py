# test_main.py

import main

def test_find_water_depth():
    # Test the find_water_depth function from main.py
    result = main.find_water_depth()
    print(f"Test result: The depth of water is approximately {result:.4f} feet.")
    assert abs(result - 0.6955) < 1e-4, f"Test failed! Expected ~0.6955, but got {result}"

if __name__ == "__main__":
    test_find_water_depth()
