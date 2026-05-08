"""
计算器

版本: v1.0.0
作者: Claude

包含加法和乘法运算
"""


def add(a, b):
    """加法运算"""
    return a + b


def multiply(a, b):
    """乘法运算"""
    return a * b


if __name__ == "__main__":
    print(f"加法: add(1, 2) = {add(1, 2)}")       # 3
    print(f"乘法: multiply(3, 5) = {multiply(3, 5)}")  # 15.0
