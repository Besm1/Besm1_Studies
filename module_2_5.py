# Рациональная функция
def get_matrix(n, m, value):
    # if n == 0 or m == 0:
    #     return []
    return [[value] * m] * n

# Функция по подсказке к заданию
def get_matrix2(n, m, value):
    matrix_ = []
    for i in range(n):
        matrix_.append([])
        for j in range(m):
            matrix_[i].append(value)
    return matrix_

print('Результат выполнения рациональной функции:')
result1 = get_matrix(0, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)

print('\nРезультат выполнения функции по подсказке к заданию:')
result1 = get_matrix2(0, 0, 10)
result2 = get_matrix2(3, 5, 42)
result3 = get_matrix2(4, 2, 13)
print(result1)
print(result2)
print(result3)

