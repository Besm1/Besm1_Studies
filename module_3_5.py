"""  Решение через целые числа без преобразования в строку получается понятнее """
def get_multiplied_digits_n(number):
    if number < 10:
        return number
    elif (number % 10) == 0:
        return get_multiplied_digits_n(number // 10)
    else:
        return (number % 10) * get_multiplied_digits_n(number // 10)


def get_multiplied_digits(number):
    number = str(number)
    if len(number) <= 1:
        return int(number)
    elif number[-1:] == '0':
        return get_multiplied_digits(int(number[:-1]))
    else:
        return int(number[-1:]) * get_multiplied_digits(int(number[:-1]))


print(get_multiplied_digits_n(40203))
print(get_multiplied_digits(40203))
