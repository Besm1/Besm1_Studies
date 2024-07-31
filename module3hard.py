
def calculate_structure_sum(*args):
    if args[0] == None or not args[0]:  # Пустой аргумент или пустая коллекция
        return 0
    if isinstance(args[0], set) or isinstance(args[0], tuple) or isinstance(args[0], list):   # Колллекция -
        lst = list(args[0])     # Преобразуем в список, т.к. у него есть метод .pop()
                                # будем откусывать и рассчитывать по одному элементу,
                                # и прибавлять сумму оставшейся части списка
        return calculate_structure_sum(lst.pop()) + calculate_structure_sum(lst)
    elif isinstance(args[0], dict):     # Словарь преобразуем в список кортежей и обработаем полученную коллекцию
        return calculate_structure_sum(list(args[0].items()))
    elif isinstance(args[0], int) or isinstance(args[0], float):  # Это число
        return args[0]
    elif isinstance(args[0], str):      # Это строка - вернём длину
        return len(args[0])




data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
