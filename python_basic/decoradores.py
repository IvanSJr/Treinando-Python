"""
def master(funcao):
    def slave(*args, **kwargs):
        print('Decorador')
        funcao(*args, **kwargs)

    return slave



def fala_oi():
    print('Oi!')


var = master(fala_oi)
var()
# Decorador
# Oi!



@master
def fala_oi_decorada():
    print('Oi!')


fala_oi_decorada()


# Decorador
# Oi!


@master
def outra_funcao(msg):
    print(msg)


outra_funcao('Olá, meu nome é Ivan!')
# Decorador
# Olá, meu nome é Ivan!


"""


from time import time, sleep


def velocidade(funct):
    """Verifica quanto tempo a função leva para ser executada."""
    def interna(*args, **kwargs):
        start_time = time()
        result = funct(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f'A função {funct.__name__} levou {tempo:.2f}')
        return result
    return interna


@velocidade
def for_func():
    for i in range(5):
        print(i)
        sleep(1)


for_func()
