"""
# https://docs.python.org/3/library/functions.html#open

# Criando arquivo

arquivo = open("criandoArquivos.txt", "w+")

arquivo.write("Escrevendo a 1 linha\nEscrevendo a 2 linha\nEscrevendo a 3 linha")

# Lendo arquivo
arquivo.seek(0, 0)  # Relativo à onde o cursor se encontra no arquivo
print('Lendo linhas:')
print(arquivo.read())

arquivo.seek(0, 0)
print(arquivo.readline(), end='')  # Vai começar da linha 1, end para não quebrar a linha
print(arquivo.readline(), end='')  # Vai começar da linha 2, end para não quebrar a linha
print(arquivo.readline(), end='')  # Vai começar da linha 3, end para não quebrar a linha

print()
arquivo.seek(0, 0)
print(arquivo.readlines())  # Vai colocar em uma lista ['Escrevendo a 1 linha\n', 'Escrevendo a 2 linha\n',
# 'Escrevendo a 3 linha']

# Iterando sobre readlines
arquivo.seek(0, 0)
for l in arquivo.readlines():
    print(l, end='')
print()
# Iterando sobre arquivo completo
arquivo.seek(0, 0)
for l in arquivo:
    print(l, end='')
arquivo.close()

# Utilizando bloco try

try:
    file = open('criandoArquivos2.txt', 'w+')
    file.write('Escrevendo com o bloco Try')
    file.seek(0)
    print(file.read())
finally:
    file.close()

# Escrita e leitura
with open('criandoArquivos3.txt', 'w+') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')
    file.write('Linha 4\n')
    file.write('Linha 5\n')

    file.seek(0)
    print(file.read())

# Leitura de arquivos
with open('criandoArquivos3.txt', 'r') as file:
    print(file.read())

# 'a+' ativa o append mode, escreve mas não apaga o conteúdo do arquivo
with open('criandoArquivos3.txt', 'a+') as file:
    file.write('Linha 6\n')
    file.seek(0)
    print(file.read())
"""


