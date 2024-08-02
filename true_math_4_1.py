from math import inf, isinf
# import math

def divide(first :float, second: float):
    if abs(second) < 1e-7:
        return inf
    else:
        return first / second
