import json

def delete(name) -> dict:
    with open('asdasdsad.json', 'r') as f:
        ludwici = json.load(f)
        for record in ludwici:
            if record['Name'] == name:
                ludwici.remove(record)
        print(ludwici)


def search(name) -> dict:
    with open('asdasdsad.json', 'r') as f:
        ludwici = json.load(f)
        for record in ludwici:
            if record['Name'] == name:
                return record


def create(name, first, second, third) -> None:
    to_record = {
        'Name': name,
        'first': first,
        'second': second,
        'third': third
    }
    ludwici = []
    with open('asdasdsad.json', 'r+') as f:
        ludwici = json.load(f)
    with open('asdasdsad.json', 'a+') as f:
        ludwici.append(to_record)
        json.dump(ludwici, f, ensure_ascii=False)



delete('ludwici')
