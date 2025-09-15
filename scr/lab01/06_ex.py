n = int(input('in_1: '))
finT = 0
finF = 0
for i in range(n):
    print('in_', i+2, ': ', end='', sep = '')
    p = str(input())
    s = p.split()
    if str(s[3]) == 'True':
        finT += 1
    else:
        finF += 1
print('out:', finT, finF)
