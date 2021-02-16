#def potenciação(a,b):
 #   print(a**b)

#potenciação(5,8)

#def soma (a,b):
#    print(a)
#    print(b)
#    print(f"{a} + {b} é igual a:")
#    print(a + b)
#soma(4,9)

'''
def soma (a, b):
    return a + b # return, retorna os valores

def multiplicação (a,b):
    return a * b

s = soma(2, 8) # return precisa de valores armazenados em uma variavel
m = multiplicação(5, 5)
print(m)
print(s)
'''
def soma(x,y): #função de soma
    print(f"a soma de {x} + {y} é igual a {x+y}")

soma(5,2)

def retornaListamaior(*list):
    print(max(list)) #soma todos os valores digitados numa lista

retornaListamaior(2,4,6,8,10,12,14,16,18,20,22) #valores adicionados

#RETORNAR ALGUM VALOR

def retorna():
    return 165
#print(retorna) não impreme,já que guarda o valor
a = retorna #colocar o valor dentro de uma variavel
print(a)

def retorno():
    return 10, 50 #primeiro valor para primeira variavel, segundo valor para segunda variavel
a, b = retorno() # a = 10 b = 50
print(a,b)