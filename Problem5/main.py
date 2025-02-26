import numpy as np

# Gompertz模型定义

def gompertz(t, K, a, r):
    return K * np.exp(-a * np.exp(-r * t))

# 定义方程组残差函数

def F(params, t_data, P_data):
    K, a, r = params

    residuals = np.array([
        K * np.exp(-a * np.exp(-r * t_data[0])) - P_data[0],
        K * np.exp(-a * np.exp(-r * t_data[1])) - P_data[1],
        K * np.exp(-a * np.exp(-r * t_data[2])) - P_data[2]
    ])
    return residuals

# 定义雅可比矩阵

def jacobian(params, t_data):
    K, a, r = params

    J = np.zeros((3, 3))
    
    for i, t in enumerate(t_data):
        exp_term1 = np.exp(-a * np.exp(-r * t))
        exp_term2 = np.exp(-r * t)
        
        # 对K的偏导

        J[i, 0] = exp_term1

        
        # 对a的偏导

        J[i, 1] = -K * exp_term1 * exp_term2

        
        # 对r的偏导

        J[i, 2] = K * a * t * exp_term1 * exp_term2 
    
    return J

# 牛顿法求解器

def newton_method(t_data, P_data, initial_guess, max_iter=100, tol=1e-6):
    params = np.array(initial_guess)
    
    for _ in range(max_iter):
        F_val = F(params, t_data, P_data)
        if np.linalg.norm(F_val) < tol:
            break

            
        J_val = jacobian(params, t_data)
        
        try:
            delta = np.linalg.solve(J_val, -F_val)
        except np.linalg.LinAlgError:
            print("矩阵奇异，尝试添加正则化")
            delta = np.linalg.lstsq(J_val, -F_val, rcond=None)[0]
        
        params += delta

        
    return params

if __name__ == "__main__":
    # 数据准备（t=0对应1960年）
    t_data = np.array([0, 10, 20])  # 1960,1970,1980

    P_data = np.array([179323, 203302, 226542])  # 单位：千人

    
    # 初始参数猜测（K应大于最大观测值）
    initial_guess = [250000, 1.0, 0.1]
    
    # 执行牛顿法

    params = newton_method(t_data, P_data, initial_guess)
    
    # 输出拟合参数

    K, a, r = params

    print(f"拟合参数:")
    print(f"K = {K:.2f} 千人")
    print(f"a = {a:.4f}")
    print(f"r = {r:.4f}")
    
    # 预测1990年（t=30）
    t_pred = 30

    prediction = gompertz(t_pred, K, a, r)
    print(f"\n1990年预测人口: {prediction:,.2f} 千人")
    
    # 验证拟合结果

    print("\n拟合验证:")
    for t, P in zip(t_data, P_data):
        fit = gompertz(t, K, a, r)
        print(f"年份 {1960 + t}: 实际={P}千人, 拟合={fit:.2f}千人, 误差={abs(P-fit):.2f}千人")