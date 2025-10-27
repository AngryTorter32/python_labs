from ..lib.text import *
text = input()
text = normalize(text, True, True)
text = tokenize(text)
print('Всего слов:', len(text))
print('Уникальных слов:', len(set(text)))
sl = []
top = top_n(text, 5)
k = top.keys()
n = list(k)
print(top, n)
#запускать командой python -m scr.lab03.text_stats
