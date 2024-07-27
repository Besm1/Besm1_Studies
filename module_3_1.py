def count_calls():
    """ Подсчёт кол-ва вызовов"""
    global calls  # Используем глобальную переменную
    calls += 1
    return


def string_info(str_):
    """ Сбор информации о строке """
    count_calls()  # Просигнализируем о вызове
    return (len(str_), str_.upper(), str_.lower())


def is_contains(str_, list_):
    count_calls()  # Просигнализируем о вызове
    contains = False  # Считаем, что такой строки в списке нет
    for i in range(0, len(list_)):
        if list_[i].lower() == str_.lower():  # сравним строки, преобразованные к одному регистру.
            contains = True  # Если есть - установим флаг и завершим поиск
            break
    return contains


calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
