import unittest

from main import bisection_method, position, x_target, g, t

class TestPendulumSolution(unittest.TestCase):
    def test_omega_value(self):
        # 获取计算结果（容差保持与主程序一致）
        omega_result = bisection_method(position, x_target, 0.01, 10, 1e-5)
        
        # 验证 omega 是否接近 0.317（允许 ±0.001 的误差）
        self.assertAlmostEqual(omega_result, 0.317, delta=0.001,
                              msg=f"ω值 {omega_result:.5f} 超出预期范围 0.317±0.001")


if __name__ == "__main__":
    unittest.main()
