import json

def students_to_json(students, path):
    data = [s.to_dict() for s in students]
    json.dumps(data, ensure_ascii=False, indent=2)

def students_from_json(path):
    return []