import random

""" 
    Программа интерактивная. При запуске сразу выбирает первое случайное значение числа-замка и рассчитывает к нему ключ,
    потом ждёт пользовательского ввода. Если с консоли юзер вводит:
    - stop - выполнение программы прекращается
    - test - происходит тестовый запуск: перебираются все допустимые значения "замка", для них происходит расчёт
                ключа и его сравнение с контрольным значением из задания, результаты выводятся группами по три
                строки (см. описание ниже) для каждого значения "замка"
    - любую другую (даже пустую) строку - выбирается очередное случайное значение числа-замка и происходит вычисление
        ключа к нему.

    После расчёта каждого ключа программа выдаёт на печать три строки: 
        1 стр.: - значение числа-замка и результат сравнения с контрольными ответами из задания (True или False)
        2 стр.: - рассчитанный ключ
        3 стр,: - контрольное значение ключа из задания для визуального коонтроля

"""


def calc_key(num):
    # Ключ будем рассчитывать функцией. На входе - число-замок, на выходе - символьный ключ
    key = ''
    for i in range(1, num // 2 + 1):  # Уникальная пара: первое число из первой половины диапазона (1, <num>),
        for j in range(i + 1, num):  #   второе число - из второй половины, но меньше, чем само число <num>
            if num % (i + j) == 0:
                key += str(i) + str(j)  # Если num делится на сумму чисел, то допишем их симв.предст. в конец ключа
    return key


# Для проверки введём массив правильных ответов из задания
check_keys = [  # Используем для визуальной проверки - это правильные ответы для любого числа от 3 до 20
    ''
    , ''
    , ''
    , '12'
    , '13'
    , '1423'
    , '121524'
    , '162534'
    , '13172635'
    , '1218273645'
    , '141923283746'
    , '11029384756'
    , '12131511124210394857'
    , '112211310495867'
    , '1611325212343114105968'
    , '1214114232133124115106978'
    , '1317115262143531341251161079'
    , '11621531441351261171089'
    , '12151811724272163631545414513612711810'
    , '118217316415514613712811910'
    , '13141911923282183731746416515614713812911'
]


def print_result(lock, key, check):
# печать 3-строчного ответа. Печатается одно и то же из двух разных веток программы, поэтому вынес в функцию.
    print(f"Замок: {lock}    {key == check}")
    print(f"   Ключ    : {key}")
    print(f"   Проверка: {check}")


answer = ''  # пользовательский ввод. Для первого раза - пусто
while answer != 'stop':
    if answer == 'test':
        print("\n*** Тест ***")
        for lock_ in range(3, 21):
            print_result(lock_, calc_key(lock_), check_keys[lock_])
    else:
        lock = random.randrange(3, 21)
        print_result(lock, calc_key(lock), check_keys[lock])

    answer = input('\ntest, stop, run? ')
    answer.lower()  # для точного сравнения
    print('')
