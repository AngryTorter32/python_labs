def top_n(t, n):
    fin = {}
    uni = set(t)
    uni = list(uni)
    uni = sorted(uni)
    kol = []
    for i in range(len(uni)):
        kol.append(t.count(uni[i]))
    kol_u = set(kol)
    kol_u = sorted(list(kol_u), reverse=True)
    for i in kol_u:
        for j in uni:
            if t.count(j) == i:
                fin.update({j:i})
    for i in range(len(fin) - n):
        fin.popitem()
    return fin
print(top_n(['привет', 'мир', 'привет', 'привет', 'мир', 'a', 'a', 't'], 2))
print(top_n(["a","b","a","c","b","a"], 2))
print(top_n(["bb","aa","bb","aa","cc"], 2))