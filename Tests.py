# # import this
#
# a = '  AbCd  '
# print('<'+a.lower()+'>')
# print('<'+a.strip()+'>')
# print('<'+a.lower().strip()+'>')
# a.lower().strip()
# print(a)
# a = a.lower().strip()
# print(a)
#
# print(' ' in a)
#
#
#
# a = {'a':1, 'b':3, 'c':5}
# print(a)
# b = list(a.items())
# print(b)
# c={1,2,3,4,5}
# print(c)
# print(c.pop())
# print(c)
# d=[1,2,33,4,5,6]
# print(d)
# print(d.pop())
# print(list(d))
# print(list(a))
# print(list(b))
#
# def prt_x():
#     nonlocal x
#
#     def ccc():
#         x += 10
#     print(x)
#
# x = 5
# prt_x()
# print(x)

res = lambda a, b, c, x: a * x ** 2 + b * x + c

print(res(1, 2, 3, 4))
