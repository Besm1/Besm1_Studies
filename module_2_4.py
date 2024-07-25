numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in range(1, len(numbers)):
    is_prime = True # Предположим, что это простое число
    for j in range(1, i-1): # Переберём делители от 2 до предыдущего числа
        if numbers[i] % numbers[j] == 0: # Нашли делитель
            not_primes.append(numbers[i]) # Значит, число не простое - добавим в список составных...
            is_prime = False  # ... и сбросим флаг простого числа
            break

    if is_prime: # Если число всё-таки простое,
        primes.append(numbers[i]) # то добавим его в список простых

print('Primes:', primes)
print('Not-Primes:', not_primes)