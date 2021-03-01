"""
Operadores ternários em python
"""

idade = input('Qual sua idade')

if idade.isnumeric():
    idade = int(idade)
    e_de_maior = (idade>=18)
    msg = 'Pode acessar' if e_de_maior else 'Não pode acessar'
    print(msg)
else:
    print('Você precisa digitar apenas números')

# if idade >= 18:
#     print('Pode acessar')
# else:
#     print('Não pode acessar')