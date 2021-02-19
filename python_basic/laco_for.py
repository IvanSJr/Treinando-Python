"""
Laço For
x = [[1,2,3,5,12], [21,4,2,3,32,12]]

for i in x: #laço for + uma variavel + in + variavel afetada
    print(i)

for w in range(0, 1002, 2): #mostra os números pares
    print(w)

varivel = ['Ivan', 'Luiz', 'Luiz Henrique', 'Luiz Felipe']

# Itera até achar a palavra Luiz
for n in varivel:
    print(n)
    if n == 'Luiz':
        break

# Itera em todos que começam com L
for n in varivel:
    if n.startswith('L'):
        print(n)

comeca_com_L = False
cont = 0
for n in varivel:
    if n.startswith('L'):
        comeca_com_L = True
        cont += 1
print(f'Existem {cont} palavras que começam com L')
"""

