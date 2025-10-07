def transpose(a):
    for i in range(len(a) - 1):
        if len(a[i]) != len(a[i + 1]):
            return "ValueError"
    if a == []:
        return []
    ansA = []
    y = len(a)
    x = len(a[0])
    for i in range(x):
        ansS = []
        for j in range(y):
            ansS.append(a[j][i])
        ansA.append(ansS)
    return ansA

def row_sums(a):
    for i in range(len(a) - 1):
        if len(a[i]) != len(a[i + 1]):
            return "ValueError"
    if a == []:
        return []
    ans = []
    for i in range(len(a)):
        ans.append(sum(a[i]))
    return ans

def col_sums(a):
    for i in range(len(a) - 1):
        if len(a[i]) != len(a[i + 1]):
            return "ValueError"
    if a == []:
        return []
    ans = []
    for j in range(len(a[0])):
        c = 0
        for i in range(len(a)):
            c += a[i][j]
        ans.append(c)
    return ans
print('transpose:')
print(transpose([[1, 2, 3]]), transpose([[1], [2], [3]]), transpose([[1, 2], [3, 4]]), sep = '\n')
print(transpose([]), transpose([[1, 2], [3]]), sep = '\n')

print(' ', 'row_sums:', sep = '\n')
print(row_sums([[1, 2, 3], [4, 5, 6]]), row_sums([[-1, 1], [10, -10]]), sep = '\n')
print(row_sums([[0, 0], [0, 0]]), row_sums([[1, 2], [3]]), sep = '\n')

print(' ', 'col_sums:', sep = '\n')
print(col_sums([[1, 2, 3], [4, 5, 6]]), col_sums([[-1, 1], [10, -10]]), sep = '\n')
print(col_sums([[0, 0], [0, 0]]), col_sums([[1, 2], [3]]), sep = '\n')
