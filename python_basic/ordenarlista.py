lista1 = [123, 325, 543, 876, 4356, 2134, 523432, 12, 41, 0]

lista1.sort() #ordena a lista numericamente 
print(lista1) 

lista = sorted(lista1) #precisa de uma variavel 
print(lista1)

lista1.sort(reverse=True) #ordena de maneira decrescente
print(lista1)

lista1.reverse() #não ordena, somente inverte os valores

lista2 = ["bola", "trapézio", "pássaro"]
lista2.sort() #ordem alfabetica

lista2.sort(reverse=True) #do z ao a