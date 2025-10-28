def normalize(text, casefold, yo2e):
    if casefold != False:
        text = text.casefold()
    if yo2e != False:
        text = text.replace('ё', 'е')
        text = text.replace('Ё', 'Е')
    text = text.replace('\n', ' ')
    text = text.replace('\t', ' ')
    text = text.replace('\r', ' ')
    text = text.replace('\b', ' ')
    spis = text.split()
    text = ''
    for i in range(len(spis)):
        text += spis[i]
        text += ' '
    text = text.strip()
    return text
def tokenize(text):
    raz = ['!', ',', '😀', '—', ':', ';', '?', '/', '&', '*', '#', '$', '%']
    for i in range(len(text)):
        if text[i] in raz:
            text = text.replace(text[i], ' ')
    spis = text.split()
    return spis
def count_freq(text):
    sl = set(text)
    sl = list(sl)
    kol = {}
    for i in range(len(sl)):
        kol.update({sl[i]:text.count(sl[i])})
    return kol
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
print('normalize:')
print(normalize("ПрИвЕт\nМИр\t", True, True), normalize('ёжик, Ёлка', True, True), sep = '\n')
print(normalize("Hello\r\nWorld", True, True), normalize("  двойные   пробелы  ", True, True), sep='\n')
print('', 'tokenize:', sep = '\n')
print(tokenize("привет мир"), tokenize("hello,world!!!"), sep = '\n')
print(tokenize("по-настоящему круто"), tokenize("2025 год"), sep = '\n')
print(tokenize("emoji 😀 не слово"))
print(' ', 'count_freq + top_n:', sep = '\n')
print('Частоты:', count_freq(["a","b","a","c","b","a"]), 'Топ:', top_n(["a","b","a","c","b","a"], 2))
print('Частоты:', count_freq(["bb","aa","bb","aa","cc"]), 'Топ:', top_n(["bb","aa","bb","aa","cc"], 2))
