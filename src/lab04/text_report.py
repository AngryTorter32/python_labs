from ..lib.text import normalize, tokenize, top_n
from ..lib.io_txt_csv import read_text, write_csv

file_name = input('Введите название файла в папке data (по умолчанию - input.txt): ') #по желанию пользователя может быть выбран другой файл
if file_name == '':
    file_path = r"C:\Users\kuzne\Desktop\laby_piton\python_labs\src\data\lab04\input.txt" #по умолчанию используется файл input.txt
else:
    file_path = r"C:\Users\kuzne\Desktop\laby_piton\python_labs\src\data\lab04" + f'\{file_name}'
cod = input('Введите кодировку файла (по умолчанию - utf-8): ') #по желанию пользователя, может быть выбрана другая кодировка
if cod == '':
    cod = 'utf-8' #по умолчанию кодировка utf-8
t = read_text(file_path, cod)
t = normalize(t, True, True)
s = tokenize(t)
uni = set(s)
top = top_n(s, len(uni))
top.insert(0, ('word', 'count'))
write_csv(top, r'C:\Users\kuzne\Desktop\laby_piton\python_labs\src\data\lab04\report.csv')
print('Всего слов: ', len(s))
print('Уникальных слов: ', len(uni))
print('Топ-5:')
top5 = top_n(s, 5)
for i in range(len(top5)):
        print(top5[i][0], ':', top5[i][1], sep = '')
