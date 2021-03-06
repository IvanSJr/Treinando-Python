def master(funct):
    def slave():
        funct()
    return slave


def fala_oi():
    print('Oi!')


master(fala_oi)


def potenciacao(a1, b2):
    print(a1 ** b2)


potenciacao(5, 8)


def soma(a3, b3):
    print(a3)
    print(b3)
    print(f"{a3} + {b3} é igual a:")
    print(a3 + b3)
    soma2(4, 9)


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


def soma2(x, y):  # função de soma
    print(f"a soma de {x} + {y} é igual a {x + y}")


soma2(5, 2)


def retornaListaMaior(*lista):
    print(max(lista))  # soma todos os valores digitados numa lista


retornaListaMaior(2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22)  # valores adicionados


# RETORNAR ALGUM VALOR

def retorna():
    return 165


# print(retorna) não impreme,já que guarda o valor
a = retorna  # colocar o valor dentro de uma variavel
print(a)


def retorno():
    return 10, 50  # primeiro valor para primeira variavel, segundo valor para segunda variavel


a, b = retorno()  # a = 10 b = 50
print(a, b)


# Utilizando o *args and **kwargs

def func(*args):
    # Caso não saiba quantos valores serão utilizados
    print(args)
    print(len(args))


func(1, 2, 3, 4, 5)


def func2(*args):
    # casting tuple para listas
    args = list(args)
    args[0] = 10  # Primeiro valor sempre será 10
    args[1] = 50  # Segundo valor sempre será 50
    print(f'{len(args)} valores')
    for i in args:
        print(i)


func2(1, 2, 4, 5, 6, 7, 8, 9, 15, 20, 23, 5, 1, 23, 4, 2)
