import argparse
from pathlib import Path
from src.lib.text import top_n, normalize, tokenize


def main():
    parser = argparse.ArgumentParser(description='Модуль CLI_text, выводит текст и статистику по нему.')
    subparsers = parser.add_subparsers(dest='command')

    # подкоманда stats
    stats_parser = subparsers.add_parser('stats', help='Частоты слов')
    stats_parser.add_argument('--input', required=True, help='Расположение файла')
    stats_parser.add_argument('--top', type=int, default=5, help='Сколько слов выводить в топе')

    # подкоманда cat
    cat_parser = subparsers.add_parser('cat', help='Выводит содержимое файла')
    cat_parser.add_argument('--input', required=True, help='Расположение файла')
    cat_parser.add_argument('-n', action='store_true', help='Нумеровать строки')

    args = parser.parse_args()

    if args.command == 'cat':
        file_path = Path(args.input)
        text = file_path.read_text(encoding='utf-8')
        text = normalize(text, True, True) 
        text_tokens = tokenize(text)
        if args.n:
            for i in range(len(text_tokens)):
                print(text_tokens[i])
        else:
            for i in range(len(text_tokens)):
                print(i, text_tokens[i])
    
    if args.command == 'stats':
        file_path = Path(args.input)
        text = file_path.read_text(encoding='utf-8')
        text = normalize(text, True, True)
        text_tokens = tokenize(text)
        text_top = top_n(text_tokens, args.top)
        for i in range(len(text_top)):
            print(text_top[i])

if __name__ == "__main__":
    main()

#python -m src.lab06.cli_text stats --input "C:\\Users\\kuzne\\Desktop\\laby_piton\\python_labs\\data\\lab06\\text.txt" --top 5
#python -m src.lab06.cli_text cat --input "C:\\Users\\kuzne\\Desktop\\laby_piton\\python_labs\\data\\lab06\\text.txt"