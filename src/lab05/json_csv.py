import json
import csv
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str):
    try:
        path_j = Path(json_path)
        path_c = Path(csv_path)
        with path_j.open('r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                raise ValueError
        if data == []:
            raise ValueError
        with path_c.open('w', newline='', encoding='utf-8') as cf:
            writer = csv.DictWriter(cf, fieldnames=['name', 'age'])
            writer.writeheader()
            writer.writerows(data)
    except FileNotFoundError:
        print('FileNotFoundError')

def csv_to_json(csv_path: str, json_path: str):
    try:
        path_j = Path(json_path)
        path_c = Path(csv_path)
        with open(path_c, encoding='utf-8') as f:
                try:
                    data = list(csv.DictReader(f))
                except csv.Error:
                    raise ValueError
        if data == []:
            raise ValueError
        with path_j.open('w', encoding='utf-8') as f_j:
            json.dump(data, f_j, ensure_ascii=False, indent=2)
    except FileNotFoundError:
        print('FileNotFoundError')

csv_to_json('C:\\Users\\kuzne\\Desktop\\laby_piton\\python_labs\\data\\samples\\people.csv', 
            'C:\\Users\\kuzne\\Desktop\\laby_piton\\python_labs\\data\\out\\people_from_csv.json')