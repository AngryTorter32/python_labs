from ..lib.text import *
text = input()
text = tokenize(text)
print('Всего слов:', len(text))
print('Уникальных слов:', len(set(text)))
ls = []
for i in range(len(text)):
    ls.append(len(text[i]))
print('Слово', ' ' * (max(ls) - len('Слово')), '| Частота', sep = '')
print('-' * max(ls), '-', '-' * len(' частота'), sep = '')
for i in range(len(set(text))):
    print(list(set(text))[i], ' ' * (max(ls) - len(list(set(text))[i])), '| ', text.count(list(set(text))[i]), sep = '')
#запускать командой python -m scr.lab03.text_stats
