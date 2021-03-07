from random import randint
import re

REGRESSIVO = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def validadora(cnpj):
    cnpj = remover_caracters(cnpj)
    try:
        if verifica_sequencia(cnpj):
            return False
    except:
        return False

    try:
        novo_cnpj = calcula_digito(cnpj=cnpj, digito=1)
        novo_cnpj = calcula_digito(cnpj=novo_cnpj, digito=2)
    except Exception as e:
        return False

    if novo_cnpj == cnpj:
        return True
    else:
        return False


def calcula_digito(cnpj, digito):
    if digito == 1:
        regressivos = REGRESSIVO[1:]
        novo_cnpj = cnpj[:-2]
    elif digito == 2:
        regressivos = REGRESSIVO
        novo_cnpj = cnpj
    else:
        return None

    total = 0
    for indice, regressivo in enumerate(regressivos):
        total += int(cnpj[indice]) * regressivo

    digito = 11 - (total % 11)
    digito = digito if digito <= 9 else 0
    return f'{novo_cnpj}{digito}'


def remover_caracters(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)


def verifica_sequencia(cnpj):
    sequencia = cnpj[0] * len(cnpj)
    if sequencia == cnpj:
        return True
    else:
        return False


def gera():
    # 40.142.724/0001-94
    primeiro_digito = randint(0, 9)
    segundo_digito = randint(0, 9)
    primeiro_bloco = randint(000, 999)
    segundo_bloco = randint(000, 999)
    zero_um = '0001'
    inicio_cnpj = f'{primeiro_digito}{segundo_digito}{primeiro_bloco}{segundo_bloco}{zero_um}00'
    novo_cnpj = calcula_digito(cnpj=inicio_cnpj, digito=1)
    novo_cnpj = calcula_digito(cnpj=novo_cnpj, digito=2)
    return novo_cnpj


def formata_cnpj(cnpj):
    cnpj = remover_caracters(cnpj)
    formatado = f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'
    return formatado

