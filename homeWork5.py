# 2. Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
immutable_var = 1, 2.5, 'kolbasa', [1, 1, 2, 3, 5, 8]
print(immutable_var)

# Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежа.
#immutable_var[2] = 'sausage'
#print(immutable_var)
print("If we try to change an element of tuple we got the error message because objects of class 'tuple' don't support item assignement")
immutable_var[3].remove(2)
print(immutable_var)
immutable_var[3].append('Helas!')
print(immutable_var)
print("Notwithstanding we can change elements and/or the structure of any mutable member of the tuple...")
immutable_var = 9,8,7
print(immutable_var)
print(" ...and even the whole tuple.\n")

# 4 - Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
#   - Измените элементы списка mutable_list.
#   - Выведите на экран измененный список mutable_list.
mutable_list = [1, 2.5, 'kolbasa', [1, 1, 2, 3, 5, 8]]
print(mutable_list)
mutable_list[2] = 'sausage'
print(mutable_list)