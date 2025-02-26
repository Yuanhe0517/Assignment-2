import unittest

from main import newton_raphson  # 假设 main.py 包含牛顿法函数

class TestPopulationEquationSolution(unittest.TestCase):
    def test_solution_near_expected(self):
        # 目标解和允许的绝对误差

        expected_solution = 0.100998

        tolerance = 0.0001  # 允许 ±0.0001 的误差

        # 运行牛顿法（初始猜测需接近真实解，否则可能收敛到其他根）
        initial_guess = 0.1  # 初始猜测值需合理

        computed_solution = newton_raphson(initial_guess=initial_guess, tol=1e-8)
        
        # 检查计算解是否在目标值附近

        self.assertAlmostEqual(
            computed_solution,
            expected_solution,
            delta=tolerance,
            msg=f"解 {computed_solution:.6f} 不在预期范围 [{expected_solution - tolerance:.6f}, {expected_solution + tolerance:.6f}] 内"
        )

if __name__ == "__main__":
    unittest.main()
