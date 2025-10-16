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
    kol = []
    for i in range(len(sl)):
        a = str(sl[i]) + ':' + str(text.count(sl[i]))
        kol.append(a)
    return kol
print('normalize:')
print(normalize("ПрИвЕт\nМИр\t", True, True), normalize('ёжик, Ёлка', True, True), sep = '\n')
print(normalize("Hello\r\nWorld", True, True), normalize("  двойные   пробелы  ", True, True), sep='\n')
print('', 'tokenize:', sep = '\n')
print(tokenize("привет мир"), tokenize("hello,world!!!"), sep = '\n')
print(tokenize("по-настоящему круто"), tokenize("2025 год"), sep = '\n')
print(tokenize("emoji 😀 не слово"))
print(' ', 'count_freq + top_n:', sep = '\n')
print(count_freq(["a","b","a","c","b","a"]))
