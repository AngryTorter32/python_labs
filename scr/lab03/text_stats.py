from ..lib.text import normalize, tokenize, top_n
text = input()
text = normalize(text, True, True)
text = tokenize(text)
print('Всего слов:', len(text))
print('Уникальных слов:', len(set(text)))
sp = top_n(text, 5)
sl = []
for i in range(len(sp)):
    sl.append(len(sp[i][0]))
m = max(sl)
print('табличный режим(on/off):')
vkl = input()
print('Топ-5:')
if m < len('Слово'):
    m = len('Слово')
if vkl == 'on':
    print('Слово', ' ' * (m - len('Слово')), '|', ' частота', sep = '')
    print('-' * m, '-' * 9, sep = '')
    for i in range(len(sp)):
        print(sp[i][0], ' ' * (m - len(sp[i][0])), '| ', sp[i][1], sep = '')
else:
    for i in range(len(sp)):
        print(sp[i][0], ':', sp[i][1], sep = '')