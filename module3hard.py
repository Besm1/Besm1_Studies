
def calculate_structure_sum(*args):
    if args[0] == None:
        return 0
    if isinstance(args[0], int) or isinstance(args[0], float):
        return args[0]
    elif isinstance(args[0], str):
        return len(args[0])
    elif isinstance(args[0], set) or isinstance(args[0], tuple) or isinstance(args[0], list) or isinstance(args[0], set):
        s = 0
        for arg in args[0]:
            s += calculate_structure_sum(arg)
        return s
    elif isinstance(args[0], dict):
        s = 0
        for k, v in args[0].items():
            s += calculate_structure_sum((k, v))
        return s




data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
