# test_main.py

import main

import main

def test_find_time_to_hit_ground():
    # Test the find_time_to_hit_ground function from main.py
    result = main.find_time_to_hit_ground()
    print(f"Test result: The time for the object to hit the ground is approximately {result:.4f} seconds.")
    assert abs(result - 25.8397) < 0.01, f"Test failed! Expected ~25.8397, but got {result}"

if __name__ == "__main__":
    test_find_time_to_hit_ground()
 