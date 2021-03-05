"""
# Aqui eu alterei o funcionamento do python utilizando o TryExcept
try:
    print(2 / 0)
except ZeroDivisionError:
    print('Não se divide por 0')


# Tratando erros em funções próprías


def dividindo(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error_func:
        print('Log: ', error_func)  # Log:  division by zero
        raise  # Sem o raise a except de fora não funciona.


try:
    print(dividindo(2, 0))
except ZeroDivisionError as error:
    print(error)  # division by zero


def divindindo2(n1, n2):
    if n2 == 0:
        raise ZeroDivisionError('O segundo valor não pode ser 0')
    return n1 / n2


# divindindo2(2, 0) ZeroDivisionError: O segundo valor não pode ser 0

try:
    print(divindindo2(2, 0))
except ZeroDivisionError as erro:
    print(erro)  # O segundo valor não pode ser 0
"""

# n = float(input('Digite um número: '))
# Digite um número: a
# Traceback (most recent call last):
#   File "C:\Users\Ferra\PycharmProjects\Treinando-Python\python_basic\raise.py", line 40, in <module>
#     n = float(input('Digite um número: '))
# ValueError: could not convert string to float: 'a'
# print(n * 5)


def convertendo_input(n):
    """ Retorna None se não for possivel converter para int ou float."""
    try:
        n = int(n)
        return n
    except ValueError:
        try:
            n = float(n)
            return n
        except ValueError:
            pass


numero = convertendo_input(input('Digite um número: '))

if numero is None:
    print(f'Erro, isso não é um número.')
else:
    print(numero * 2)
