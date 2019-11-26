lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = ["Colar", "de", "perólas"]
lista3 = [1, "colar", "de", "perolas"]

print(lista1[2]) #printa o 3 item da lista1

for i in lista3:
    print(i) #printa todos os itens da lista selecionada

tamanho = len(lista1)
print(tamanho) #len diz qual a quantidade de itens

lista1.append(11) #adiciona itens
print(lista1)

if 6 in lista1:      #pergunta se o número ou item está na lista
    print("Olá, 6 está na lista")

del lista1[:7] #[:]
print(lista1)