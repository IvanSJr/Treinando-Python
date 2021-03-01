x = {"Nome": "Caio", "Idade": 19, "Cidade": "Lauro de Freitas", "Tel": "071 99108-5709"}

print(x['Idade'])

# DICIONARIO DENTRO DE LISTAS

cadastroPessoas = [
    {"Nome": "Caio", "Idade": 19, "Cidade": "Lauro de Freitas", "Tel": "071 99108-5709", "CPF": "05403403454"},
    {"Nome": "Ivan", "Idade": 18, "Cidade": "Salvador", "Tel": "071 99231-5229", "CPF": "12466203994"}]
print(cadastroPessoas[0]["Nome"])  # variavel [posição dentro da lista][qual indice do dicionário]
print(cadastroPessoas[0]["Tel"])


d1 = {'chave1': 12, 'nova_chave': 13}
print(d1['nova_chave'])  # Acessando indices

# Criando pelo construtor dict

d2 = dict(chave1='12', nova_chave=13)
print(d2['nova_chave'])  # Acessando indices


# Qualquer tipo de cado pode ser uma chave, geralmente uma string.

d3 = {
    'str': 'String',
    123: 'Inteiros',
    (1, 2, 3): 'Tuplas',
}

print(d3[(1, 2, 3)])  # Imprime tuplas
# print(d3['strd'])  # Esse valor não existe imprimirá um KeyError

# Utilizando o .get

print(d3.get('strd')) # Se não existir retorna None

if d3.get('strd') is not None:
    print(d1.get('strd'))
else:
    print('Não existe no dicionário!')

# Utilizando o .update

d3.update({'str': 'valor string'})  # atualizando o valor da chave 'str'
print(d3)

# Utilizando o .del

del d3[123] # removendo a chave 123
print(d3)

# Verificando valores nos dicionários

print('str' in d3)  # Verifica se existe 'str' no dicionário True
print('str' in d3.keys())  # Verifica se existe 'str' nas chaves do dicionário True
print('str' in d3.values())  # Verifica se existe 'str' nos valores do dicionário False


clientes = {
    'cliente_vip': {
        'nome': 'Ivan',
        'sobrenome': 'Júnior'
    },
    'cliente_premium': {
        'nome': 'Carmen',
        'sobrenome': 'Gomes',
    },
    'clientes_prime': {
        'nome': 'João',
        'sobrenome': 'Victor',
    }
}

# Iterando em dicionários

for k, v in d3.items():
    print(f'Chave: {k}, Valor: {v}')

for k, v in clientes.items():
    print(f'Exibindo tipos clientes {k}')
    for dados_k, dados_v in v.items():
        print(f'\t{dados_k} = {dados_v}')

# Fazendo cast para dicionários

lista1 = [
    ['c1', 2], ['c2', 3], ['c3', 4]
]

d1 = dict(lista1)
print(d1)