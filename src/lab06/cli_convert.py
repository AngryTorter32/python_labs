#python -m src.lab06.cli_convert json2csv --input "C:\Users\kuzne\Desktop\laby_piton\python_labs\data\lab06\test.json" --output 'C:\Users\kuzne\Desktop\laby_piton\python_labs\data\lab06\test.csv'
import argparse
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.cvs_xlsx import csv_to_xlsx


def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv") #дописать везде help
    p1.add_argument("--input", dest="input", required=True)
    p1.add_argument("--output", dest="output", required=True)

    p2 = sub.add_parser("csv2json")
    p2.add_argument("--input", dest="input", required=True)
    p2.add_argument("--output", dest="output", required=True)

    p3 = sub.add_parser("csv2xlsx")
    p3.add_argument("--input", dest="input", required=True)
    p3.add_argument("--output", dest="output", required=True)

    args = parser.parse_args()

    if args.cmd == 'json2csv':
        json_to_csv(args.input, args.output)
    elif args.cmd == 'csv2json':
        csv_to_json(args.input, args.output)
    elif args.cmd == 'csv2xlsx':
        csv_to_xlsx(args.input, args.output)

if __name__ == "__main__":
    main()