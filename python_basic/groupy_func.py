from itertools import groupby

alunos = [
    {'nome': 'Ivan', 'nota': 'A'},
    {'nome': 'Paulo', 'nota': 'F'},
    {'nome': 'João', 'nota': 'B'},
    {'nome': 'Erick', 'nota': 'A'},
    {'nome': 'Messias', 'nota': 'A'},
    {'nome': 'Carmen', 'nota': 'C'},
    {'nome': 'Felipe', 'nota': 'E'},
]

order = lambda item: item['nota']
alunos.sort(key=order)
alunos_groupy = groupby(alunos, order)

for agrupamento, valores_agrupados in alunos_groupy:
    print(f'Alunos tiraram notas: {agrupamento}')
    for aluno in valores_agrupados:
        print(f'Aluno: {aluno["nome"]}')
    print()
