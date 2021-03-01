from itertools import count

contador = count(start=1, step=-1)  # 0 -> -1 -> -2
contador = count(start=1, step=1)  # 1 -> 2 -> 3
for i in contador:
    if i != 10:
        print(i)
    else:
        break

# Adicionando indices a listas usando o count
contador_lista = count(start=1)
lista = ['João', 'Maria', 'Felipe', 'Flávio']
index_lista = zip(contador_lista, lista)
print(list(index_lista))