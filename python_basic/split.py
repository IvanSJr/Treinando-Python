"""
Função split
lista1 = string.split(' ')
palavra = ''
contagem = 0
for n in lista1:
    qtd_vezes = lista1.count(n)
    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = n

print(f'A palavra que apareceu mais vezes é "{palavra}" {contagem}x')

lista2 = string.split(',')
for n in lista2:
    print(n)
"""

string = "O rato roeu a roupa do rei de roma roma roma roma, Testando a lista2"
