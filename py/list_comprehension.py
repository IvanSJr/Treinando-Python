listax = [1,2,3,5]
listay = [i **2  for i in listax]  # [valor a adicionar    laço     condição ] #elevar todos os números de uma lita
listaz = [i for i in listax if i%2==0] #imprimir números pares
print(listay)
print(listaz)
