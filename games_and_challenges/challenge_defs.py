# Desafio 1
"""
1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da
função2 executada.
"""

def func1():
    return 1 +2


def func2(funcao):
    return funcao()


print(func2(func1))

# Desafio 2
"""
2 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da
função2 executada. Faça a função1 executar duas funções que recebam um número 
diferente de argumentos.
"""


def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f'Oi {nome}'


def recepcao(nome, saudacao):
    return f'{saudacao}, {nome}'


exece = mestre(fala_oi, 'Ivan')
exece2 = mestre(recepcao, 'Ivan', 'Bom Dia')
print(exece)
print(exece2)
