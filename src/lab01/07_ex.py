s = str(input('in: '))
w = []
for i in range(len(s)):
    w.append(s[i])
for i in range(len(w)):
    if w[i].isupper():
        n1 = i
        break
for i in range(len(w)):
    if w[i].isdigit():
        n2 = i + 1
        break
r = n2 - n1
k = (len(s) - n2) // r
fin = w[n1] + w[n2]
for i in range(1, k + 1):
    fin = fin + w[n2 + r * i]
print('out:', fin)
