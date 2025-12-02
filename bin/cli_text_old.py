# # import argparse
# # from pathlib import Path
# # from src.lib.text import top_n, normalize, tokenize


# # def main():
# #     parser = argparse.ArgumentParser(description='Модуль CLI_text, выводит текст и статистику по нему.')
# #     subparsers = parser.add_subparsers(dest='command')

# #     # подкоманда stats
# #     stats_parser = subparsers.add_parser('stats', help='Частоты слов')
# #     stats_parser.add_argument('--input', required=True)
# #     stats_parser.add_argument('--top', type=int, default=5)

# #     # подкоманда cat
# #     cat_parser = subparsers.add_parser('cat', help='Выводит содержимое файла')
# #     cat_parser.add_argument('--input', required=True)
# #     cat_parser.add_argument('-n', action='store_true', help='Нумеровать строки')

# #     args = parser.parse_args()

# #     if args.command == 'cat':
# #         file_path = Path(args.input)
# #         text = str(file_path.open(encoding='utf-8'))
# #         text = normalize(text, True, True) 
# #         text_tokens = tokenize(text)
# #         if args.n:
# #             for i in range(len(text_tokens)):
# #                 print(text_tokens[i])
# #         else:
# #             for i in range(len(text_tokens)):
# #                 print(i, text_tokens[i])
    
# #     if args.command == 'stats':
# #         file_path = Path(args.input)
# #         text = str(file_path.open(encoding='utf-8'))
# #         text = normalize(text, True, True)
# #         text_tokens = tokenize(text)
# #         text_top = top_n(text_tokens, args.top)
# #         for i in range(len(text_top)):
# #             print(text_top[i])

#python -m src.lab06.cli_text stats --input "C:\Users\kuzne\Documents\GitHub\python_labs\data\text.txt" -- top 5
#
'''
import argparse
from pathlib import Path
from src.lib.text import top_n, normalize, tokenize


def main():
    parser = argparse.ArgumentParser(description='Модуль CLI_text, выводит текст и статистику по нему.')
    subparsers = parser.add_subparsers(dest='command')

    # подкоманда stats
    stats_parser = subparsers.add_parser('stats', help='Частоты слов')
    stats_parser.add_argument('--input', required=True)
    stats_parser.add_argument('--top', type=int, default=5)

    # подкоманда cat
    cat_parser = subparsers.add_parser('cat', help='Выводит содержимое файла')
    cat_parser.add_argument('--input', required=True)
    cat_parser.add_argument('-n', action='store_true', help='Нумеровать строки')

    args = parser.parse_args()

    if args.command == 'cat':
        file_path = Path(args.input)
        with file_path.open(encoding='utf-8') as f:
            text = f.read()
        text = normalize(text, True, True) 
        text_tokens = tokenize(text)
        if args.n:
            for i in range(len(text_tokens)):
                print(i, text_tokens[i])
        else:
            for i in range(len(text_tokens)):
                print(text_tokens[i])
    
    if args.command == 'stats':
        file_path = Path(args.input)
        with file_path.open(encoding='utf-8') as f:
            text = f.read()
        
        # Применяем нормализацию и токенизацию
        text = normalize(text, True, True)
        text_tokens = tokenize(text)
        
        # Получаем топ-N слов
        text_top = top_n(text_tokens, args.top)
        
        # Выводим результат
        for word, count in text_top:
            print(f"{word}: {count}")


# ДОБАВЬТЕ ЭТИ СТРОКИ В КОНЕЦ ФАЙЛА:
if __name__ == '__main__':
    main()

#python src/lab06/cli_text.py stats --input "C:\Users\kuzne\Documents\GitHub\python_labs\data\text.txt" -- top 5
'''
import argparse
from pathlib import Path
from src.lib.text import top_n, normalize, tokenize


def main():
    parser = argparse.ArgumentParser(description='Модуль CLI_text, выводит текст и статистику по нему.')
    subparsers = parser.add_subparsers(dest='command')

    # подкоманда stats
    stats_parser = subparsers.add_parser('stats', help='Частоты слов')
    stats_parser.add_argument('--filedir', required=True)
    stats_parser.add_argument('--top', type=int, default=5)

    # подкоманда cat
    cat_parser = subparsers.add_parser('cat', help='Выводит содержимое файла')
    cat_parser.add_argument('--input', required=True)
    cat_parser.add_argument('-n', action='store_true', help='Нумеровать строки')

    args = parser.parse_args()

    if args.command == 'cat':
        file_path = Path(args.input)
        text = str(file_path.open(encoding='utf-8'))
        text = normalize(text, True, True) 
        text_tokens = tokenize(text)
        if args.n:
            for i in range(len(text_tokens)):
                print(text_tokens[i])
        else:
            for i in range(len(text_tokens)):
                print(i, text_tokens[i])
    
    if args.command == 'stats':
        file_path = Path(args.filedir)
        text = str(file_path.open(encoding='utf-8'))
        text = normalize(text, True, True)
        text_tokens = tokenize(text)
        text_top = top_n(text_tokens, args.top)
        for i in range(len(text_top)):
            print(text_top[i])

#python -m src.lab06.cli_text stats --input "C:\\Users\\kuzne\\Documents\\GitHub\\python_labs\\data\\text.txt" -- top 5