my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

# Рациональный вариант
i = 0
while i < len(my_list) and my_list[i] >= 0:
    if my_list[i] > 0:
        print(my_list[i])
    i = i + 1

""" Если уж по условиям задачи надо обязательно использовать операторы
    прерывания/продолжения цикла, то напишем ещё один цикл:
"""
print('\nВторой заход:')
i = 0
while i < len(my_list):
    if my_list[i] == 0:
        i = i + 1
        continue
    elif my_list[i] < 0:
        break
    else:
        print(my_list[i])
        i = i + 1
