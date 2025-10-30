## Лабораторная_03</h1>
### задание A
```python
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
    raz = ['!', ',', '😀', '—', ':', ';', '?', '/', '&', '*', '#', '$', '%', '.']
    for i in range(len(text)):
        if text[i] in raz:
            text = text.replace(text[i], ' ')
    spis = text.split()
    return spis
def count_freq(t):
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
    return fin
def top_n(t, n):
    fin = []
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
                fin.append((j, i))
    fin_s = []
    if n > len(uni):
        n = len(uni)
    for i in range(n):
        fin_s.append(fin[i])
    return fin_s
'''
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
'''
```
![text](https://github.com/user-attachments/assets/d59ba110-70f5-416f-93a8-a5af2e75a446)
normalize: 
Для начала реализую работу casefold и yo2e при помощи .replace и .casefold, затем, в цикле перебираю текст, чтобы собрать его в готовом виде.
tokenize:
Создаю список со всеми разделителями, при помощи цикла и функции replace заменяю их в тексте на пробелы. Превращаю текст в список функцией split.

count_freq:
Сначала, через множество и sorted создаю список уникальных слов из текста по алфавиту, затем нахожу их частоту в тексте так, чтобы у слова и его частоты в списке был одинаковый индекс. Уже знакомым способом создаю список уникальных значений частот, а затем перебирая уникальные значения в порядке убывания, добавляю в словарь пары слово:частота.

top_n:
Делаю все аналогично функции count_freq, за исключением того, что в конце вместо словаря используется список и кортежи вида (слово, частота). После получения списка с кортежами, я создаю его финальный вариант, куда добавляю топ-5 значений по величине, если уникальных слов меньше, n принимает значение их количества.

### задание B
```python
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

```

![text_stats](https://github.com/user-attachments/assets/fe689c82-02e7-462d-b0e8-f0bde2bf3010)
![text_stats_on_off](https://github.com/user-attachments/assets/8038aff2-fb17-41d7-a8fc-898042e25a6a)

В начале, при помощи относительного импорта добавляю функции normalize, tokenize, top_n. Затем провожу вводимый пользователем текст через функции normalize и tokenize, чтобы получить список слов. Далее нахожу сколько всего слов при помощи длинны этого списка, и сколько из них уникальных, создавая из списка множество. Далее стоит переключатель, он решает в каком виде будет производиться вывод. В случае обычного вывода, текст проходит через top_n и выводит значения по порядку, но в случае табличного, сначала необходимо найти длинну самого длинного слова в топе, под него подстраивается вся таблица, только не в случае если оно короче заголовка. Таблица выводится при помощи умножения символов по формуле ((длинна самого большого слова) - (длинна выводимого слова)) * (" "), а разделяющая полоска просто умножением "-" на длинну макс. слова + длинну остальной строки. Далее вставляю примеры текстов и выводов программы:
```
1) Сшит колпак да не по-колпаковски, вылит колокол да не по-колоколовски. Надо колпак переколпаковать, перевыколпаковать, надо колокол переколоколовать, перевыколоколовать
Всего слов: 18
Уникальных слов: 13
табличный режим(on/off):
on
Топ-5:
Слово  | частота
----------------
да     | 2
колокол| 2
колпак | 2
надо   | 2
не     | 2
2)На дворе дрова, за двором дрова, дрова вширь двора, не вместит двор дров, надо дрова выдворить на дровяной двор.
Всего слов: 19
Уникальных слов: 15
табличный режим(on/off):
off
Топ-5:
дрова:4
на:2
вместит:1
вширь:1
выдворить:1
3)Может бахнем? Обязательно бахнем, только не сейчас.
Всего слов: 7
Уникальных слов: 6
табличный режим(on/off):
on
Топ-5:
Слово      | частота
--------------------
бахнем     | 2
может      | 1
не         | 1
обязательно| 1
сейчас     | 1
```
