def min_max(a):
    if len(a) > 0:
        return (min(a), max(a))
    else:
        return 'ValueError'
def unique_sorted(b):
    b = set(b)
    b = sorted(list(b))
    return b
def flatten(c): #!!!!!!!!!!!!
    d = []
    for i in range(len(c)):
        if (type(c[i]) == int) or (type(c[i]) == str):
            d.append(c[i])
        else:
            d.extend(c[i])
    return d
print('min_max:')
print(min_max([3, -1, 5, 5, 0]), min_max([42]), min_max([-5, -2, -9]), sep = '\n')
print(min_max([]), min_max([1.5, 2, 2.0, -3.1]), sep = '\n')
print('unique_sorted:')
print(unique_sorted([3, 1, 2, 1, 3]), unique_sorted([]), sep = '\n')
print(unique_sorted([-1, -1, 0, 2, 2]), unique_sorted([1.0, 1, 2.5, 2.5, 0]), sep = '\n')
print('flatten:')
print(flatten([[1, 2], [3, 4]]), flatten(([1, 2], (3, 4, 5))), flatten([[1], [], [2, 3]]), sep = '\n')
print(flatten([[1, 2], "ab"])) #!!!!!!!!!!!!!!!
