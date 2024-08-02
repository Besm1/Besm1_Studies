def divide(first :float, second: float):
    if abs(second) < 1e-7:
        return '*Ошибка, деление на 0*'
    else:
        return first / second