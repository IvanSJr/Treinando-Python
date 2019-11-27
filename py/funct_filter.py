def pares(i):    #função para valores pares
    if i % 2 == 0:
        return i
def impar(i):    #função para valores impares
    if i% 2 == 1:
        return i

lista = [1, 2, 3, 4, 5, 6, 230]
list_impar = [filter(pares, lista)]
list_par = [filter(pares, lista)]
print(list(list_par))    #para não retornar no tipo filter, função list
print(list(list_impar))
