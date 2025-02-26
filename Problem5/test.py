# test.py

import subprocess

import re

import sys

def extract_prediction(output):
    # 匹配两种可能的输出格式（带千分位逗号和不带）
    patterns = [
        r"1990年预测人口:\s*([\d,]+\.\d+)",
        r"1990年预测人口:\s*(\d+\.\d+)"
    ]
    
    for pattern in patterns:
        match = re.search(pattern, output)
        if match:
            value_str = match.group(1).replace(',', '')
            return float(value_str)
    
    raise ValueError("无法从输出中提取预测值，请检查main.py的输出格式")

def run_test():
    try:
        # 运行main.py并捕获输出

        result = subprocess.run(
            [sys.executable, "main.py"],
            check=True,
            capture_output=True,
            text=True

        )
        output = result.stdout

        # 提取预测值

        prediction = extract_prediction(output)
        
        # 设置验证范围

        expected_min = 248500  # 249000 - 500

        expected_max = 249500  # 249000 + 500

        # 输出详细信息

        print("\n" + "="*50)
        print("测试详情：")
        print(f"获取到的完整输出：\n{output}")
        print("\n验证结果：")
        print(f"预测值: {prediction:,.2f} 千人")
        print(f"接受范围: {expected_min:,.0f} - {expected_max:,.0f} 千人")

        # 验证预测结果

        if expected_min <= prediction <= expected_max:
            print("✅ 测试通过：预测值在允许范围内")
            return 0

        else:
            print(f"❌ 测试失败：预测值 {prediction:,.2f} 超出预期范围")
            return 1

    except subprocess.CalledProcessError as e:
        print(f"❌ main.py执行失败：\n{e.stderr}")
        return 2

    except Exception as e:
        print(f"❌ 发生意外错误：{str(e)}")
        return 3

if __name__ == "__main__":
    sys.exit(run_test())