from io_txt_csv import read_text, write_csv
txt = read_text(r"C:\Users\kuzne\Desktop\laby_piton\python_labs\src\data\lab04\input.txt")  # должен вернуть строку
write_csv([("word","count"),("test",3)], "data/check.csv")  # создаст CSV