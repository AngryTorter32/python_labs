from src.lib.text import normalize, tokenize, top_n
from io_txt_csv import read_text, write_csv

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
print(s)
