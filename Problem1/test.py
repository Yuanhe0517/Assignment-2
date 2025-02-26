# test.py

import unittest

from main import bisection_method, volume, V_target, L, r

class TestTroughSolution(unittest.TestCase):
    def test_h_value(self):
        # 调用二分法求解 h（容差保持与主程序一致）
        h_result = bisection_method(volume, V_target, 0, 1, 1e-5)
        
        # 验证 h 是否接近 0.166（允许 ±0.001 的误差）
        self.assertAlmostEqual(h_result, 0.166, delta=0.001,
                              msg=f"h 值 {h_result:.4f} 超出预期范围 0.166±0.001")

if __name__ == "__main__":
    unittest.main()
