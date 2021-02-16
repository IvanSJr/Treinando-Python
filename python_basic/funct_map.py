def dobro(x):
    return x * 2

valor = 2
print(dobro(valor))
valor = [2,5,2,5,1]
print(dobro(valor)) #vai dobrar a quantidade de números da lista
#map(dobro, valor) 2 argumentos a função e a lista
print(list(map(dobro, valor)))