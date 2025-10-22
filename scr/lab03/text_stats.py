from ..lib.text import *
text = input()
text = normalize(text, True, True)
text = tokenize(text)
print('Всего слов:', len(text))
print('Уникальных слов:', len(set(text)))
ls = []
for i in range(len(text)):
    ls.append(len(text[i]))
print('Слово', ' ' * (max(ls) - len('Слово')), '| Частота', sep = '')
print('-' * max(ls), '-', '-' * len(' частота'), sep = '')
top = top_n(text, 5)
for i in range(len(top)):
    print(text[i], ' ' * (max(ls) - len(text[i])), '| ', top.get(text[i]))
print(text, top)
#запускать командой python -m scr.lab03.text_stats
