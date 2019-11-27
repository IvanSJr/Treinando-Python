#A função zip faz a concatenação entre listas
lista1 = [2,5,3,2,33]
lista2 = ["pães", "litros de leite", "litros de agua", "sorvetes", "abacates"]
lista3 = ["unid", "ml", "ml", "unid", "unid"]

for numero, letras, unidades in zip (lista1, lista2, lista3):
    print(numero, letras, unidades)
