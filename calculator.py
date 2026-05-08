"""
计算器

版本: v1.1.0
作者: Claude

包含加法、乘法和除法运算
"""


def add(a: float, b: float) -> float:
    """加法运算"""
    return a + b


def multiply(a: float, b: float) -> float:
    """乘法运算"""
    return a * b


def divide(a: float, b: float) -> float:
    """除法运算"""
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b


if __name__ == "__main__":
    print(f"加法: add(1, 2) = {add(1, 2)}")              # 3
    print(f"乘法: multiply(3, 5) = {multiply(3, 5)}")  # 15.0
    print(f"除法: divide(10, 2) = {divide(10, 2)}")    # 5.0
