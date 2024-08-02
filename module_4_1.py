from true_math_4_1 import divide as true_divide
from fake_math_4_1 import divide as fake_divide

result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)
print()
print(f'true_divide: 25 / 3 =', true_divide(25, 3))
print(f'fake_divide: 25 / 3 =', fake_divide(25, 3))
print()
print(f'true_divide: 25 / 0 =', true_divide(25, 0))
print(f'fake_divide: 25 / 0 =', fake_divide(25, 0))


