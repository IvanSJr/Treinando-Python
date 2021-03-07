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
        regressivo = REGRESSIVO[1:]
        novo_cnpj = cnpj[:-2]
    elif digito == 2:
        regressivo = REGRESSIVO
        novo_cnpj = cnpj
    else:
        return None

    total = 0
    for indice, regressivo in enumerate(regressivo):
        total += int(cnpj[indice]) * regressivo

    digito = 11 - (total % 11)
    digito = digito if digito <= 9 else 0
    return f'{novo_cnpj}{digito}'


def remover_caracters(cnpj):
    cnpj = cnpj.replace('.', '')
    cnpj = cnpj.replace('-', '')
    cnpj = cnpj.replace('/', '')
    return cnpj


def verifica_sequencia(cnpj):
    sequencia = cnpj[0] * len(cnpj)
    if sequencia == cnpj:
        return True
    return False
