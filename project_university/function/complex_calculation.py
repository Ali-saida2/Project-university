import math


def complex_calculation(x, y, z):

    if x + y < 0:
        raise ValueError("Invalid square root")

    if z == 0:
        raise ValueError("Division by zero")

    if z < 0 or not isinstance(z, int):
        raise ValueError("Invalid factorial input")

    result = ((x**2 + y**2) / z) + (math.sqrt(x + y) * math.factorial(z))

    return result