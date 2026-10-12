"""Week05 - 单摆周期模拟（小角度近似）
实验者：夏尚晨 7903126023
"""
import math

# 从 params.toml 对应的实验参数
LENGTH_M = 1.00
GRAVITY = 9.794
INITIAL_ANGLE_DEG = 15.0
SAMPLE_COUNT = 30


def theoretical_period(length: float, g: float) -> float:
    """小角度近似周期公式 T = 2π√(L/g)"""
    return 2 * math.pi * math.sqrt(length / g)


def simulate_periods(n: int) -> list[float]:
    """模拟 n 次全振动计时（含 ±0.01s 仪器精度内的微小扰动）"""
    period = theoretical_period(LENGTH_M, GRAVITY)
    # 模拟每次测量的系统偏差
    return [round(period + 0.002 * math.sin(i), 3) for i in range(n)]


if __name__ == "__main__":
    data = simulate_periods(SAMPLE_COUNT)
    mean = sum(data) / len(data)
    print(f"摆长 {LENGTH_M} m | 理论周期 {theoretical_period(LENGTH_M, GRAVITY):.3f} s")
    print(f"{SAMPLE_COUNT} 次测量均值: {mean:.3f} s")
