
def calculate_structure_sum(*args):
    if args[0] == None or not args[0]:
        return 0
    if isinstance(args[0], int) or isinstance(args[0], float):
        return args[0]
    elif isinstance(args[0], str):
        return len(args[0])
    elif isinstance(args[0], set) or isinstance(args[0], tuple) or isinstance(args[0], list):
        lst = list(args[0])
        return calculate_structure_sum(lst.pop()) + calculate_structure_sum(lst)
    elif isinstance(args[0], dict):
        return calculate_structure_sum(list(args[0].items()))




data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
