from itertools import zip_longest, count

indice = count(start=1)
estados = ['Bahia', 'São Paulo', 'Minas Gerais', 'Rio Grande do Sul', 'Rio de Janeiro', 'Acre']
siglas = ['BA', 'SP', 'MG', 'RS', 'RJ']
capitais = ['Salvador', 'São Paulo', 'Belo Horizonte', 'Porto Alegre', 'Rio de Janeiro', 'Rio Branco']
estados_siglas_capitais = zip(indice, estados, siglas, capitais)  # Não utilizar zip_longest por que pode gerar um loop
# print(estados_siglas) <zip object at 0x0187FA48>

for es in estados_siglas_capitais:
    print(es)
