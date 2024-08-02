from true_math_4_1 import divide as true_divide
from fake_math_4_1 import divide as fake_divide

print(f'true_divide: 25 / 3 =', true_divide(25, 3))
print(f'fake_divide: 25 / 3 =', fake_divide(25, 3))
print()
print(f'true_divide: 25 / 0 =', true_divide(25, 0))
print(f'fake_divide: 25 / 0 =', fake_divide(25, 0))


