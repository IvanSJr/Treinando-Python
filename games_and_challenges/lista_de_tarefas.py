def mostrar_lista(lista):
    print(f'Taraferas: {lista} ')


def adicionar(lista, valor):
    lista.append(valor)


def desfazer(lista, refazer_lista):
    if not lista_main:
        print('Não a o que desfazer!')
        return
    removendo = lista.pop()
    refazer_lista.append(removendo)
    print(f'Taraferas: {lista} ')


def refazer(lista, refazer_lista_refazer):
    if not refazer_lista_refazer:
        print('Nada a refazer!')
        return
    refazendo = refazer_lista_refazer.pop()
    lista.append(refazendo)
    print(f'Taraferas: {lista} ')


lista_main = []
refazer_list = []

while True:
    comando = input('Digite um tarefa ou desfazer, refazer, listar: ')
    if comando.lower() == 'listar':
        mostrar_lista(lista_main)
    elif comando.lower() == 'desfazer':
        desfazer(lista_main, refazer_list)
    elif comando.lower() == 'refazer':
        refazer(lista_main, refazer_list)
    else:
        adicionar(lista_main, comando)
