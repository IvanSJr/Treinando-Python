"""
Enumerate - Enumerar elementos de um iteravel (lista)
Ela retorna tuplas.
"""

string = ' O Brasil é penta'
lista1 = string.split(' ')
lista2 = [
    [0, 'Luiz'],
    [1, 'João'],
    [2, 'Ivan'],
    [3, 'Pedro']
]
lista3 = ['Luiz', 'João', 'Ivan', 'Pedro']
lista4 = [
    # 0        # 1          #2
    ['Luis','Flavio', 'Evellyn'],  # 0
    ['Pedro', 'Maria', 'Eduardo'],  # 1
    ['Helena', 'Ed', 'Jô']  # 2
]

# for indice, valor in enumerate(lista1):
#     print(indice, valor, lista1[indice])
#
# # As duas listas fazem a mesma coisa
# for indice, nome in lista2:
#     print(indice, nome)
#
# for indice, nome in enumerate(lista3):
#     print(indice, nome)

# Enumerando a lista
enumarada = enumerate(lista4)  # print(enumarada) <enumerate object at 0x020AFDA8>
enumarada = list(enumerate(lista4))
"""
Fazendo TypeCast
print(enumarada) 
[
(0, ['Luis', 'Flavio', 'Evellyn']), 
(1, ['Pedro', 'Maria', 'Eduardo']), 
(2, ['Helena', 'Ed', 'Jô'])
]
print(enumarada[0])  # (0, ['Luis', 'Flavio', 'Evellyn'])
print(enumarada[0][0])  # 0
print(enumarada[0][1])  # ['Luis', 'Flavio', 'Evellyn']
print(enumarada[0][1][1])  # Flavio
"""

for v1 in enumerate(lista4):
    valor

