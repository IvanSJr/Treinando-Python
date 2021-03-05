from vendas.formata import preco


def aumento_preco(valor , porc, formata=False):
    r = valor + (valor * porc/100)
    if formata:
        return preco.real(r)
    return r


def reduz_preco(valor, porc, formata=False):
    r = valor - (valor * porc/100)
    if formata:
        return preco.real(r)
    return r
