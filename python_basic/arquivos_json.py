import json

pessoas = {
    'alunos': {
        'a1': 'Ivan Santos',
        'a2': 'Natã Romão',
        'a3': 'Sergio Filho',
        'a4': 'Pericles Souza',
    },
    'professores': {
        'p1': 'Rogério Vasoller',
        'p2': 'Flavio Calhau',
        'p3': 'Alex Paixão',
        'p4': 'Jeferson Souza',
    }
}

json_pessoas = json.dumps(pessoas, indent=True)

with open('my_json', 'w+') as file:
    file.write(json_pessoas)

# Fazer a leitura no arquivo ler.json.py