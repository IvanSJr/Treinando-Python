# listax = [1, 3, 2, 5]
# listay = [i ** 2 for i in listax]  # [valor a adicionar    laço     condição ] #elevar todos os números de uma lita
# listaz = [i for i in listax if i % 2 == 0]  # imprimir números pares
# print(listay)
# print(listaz)

# Atulizando arquivos de list_comprehension

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [i * 2 for i in l1]  # Multipliquei cada elemento por 2
l3 = [(i, i2) for i in l1 for i2 in range(3)]  # Criando cordenadas [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)...]
l1 = ['Ivan', 'Igor', 'Iago']
l4 = [i.replace('I', 'Y').title() for i in l1]  # Trocando o I por Y em todos os elementos da lista.

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor3'),
    ('chave3', 'valor3'),
)
l5 = [(x, y) for x, y in tupla]  # iterando nas tuplas com list compreehension
l5 = dict(l5)  # Transformando em um dicionário

l1 = list(range(1, 100))
l6 = [i for i in l1 if i % 3 == 0 if i % 4 == 0]  # Retorna todos os multiplos de 3 e 4.
l7 = [i if i % 3 != 0 else f'É {i} divisivel por 3' for i in l1]  # Retorna todos os núemros que são divisiveis por 3
print(l7)
