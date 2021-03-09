"""
public = Metôdos e atributos que podem ser acessados dentro e fora da classe
protected  =São atribuos e metodos que podem ser acessados apenas dentro da classe ou das filhas da classe
private = São atributos e metodos que só podem ser acessados dentro da classe

Acesso:
    protected (_public)
    private (_NOMEDACLASSE__nomeatributo)
"""
"""

class BaseDeDados:

    def __init__(self):
        self.dados = {}

    def listagem_clientes(self):
        for id_cliente, nome in self.dados['clientes'].items():
            print(id_cliente, nome)

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.dados:
            self.dados['clientes'] = {id: nome}
        else:
            self.dados['clientes'].update({id: nome})

    def apaga_cliente(self, id):
        del self.dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_cliente(1, 'Otávio')
bd.inserir_cliente(2, 'João')
bd.inserir_cliente(3, 'Felipe')
bd.inserir_cliente(4, 'Pedro')
bd.inserir_cliente(5, 'Guilherme')
bd.apaga_cliente(3)
bd.dados = 'aaaaaaaaa'  # Quebrei os metodos da classe
bd.listagem_clientes()"""


# Solução


class BaseDeDados:

    def __init__(self):
        self.__dados = {}

    def listagem_clientes(self):
        for id_cliente, nome in self.__dados['clientes'].items():
            print(id_cliente, nome)

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


# _ -> protected
# __ -> privada proibe de acessar
bd2 = BaseDeDados()
bd2.inserir_cliente(1, 'Otávio')
bd2.inserir_cliente(2, 'João')
bd2.inserir_cliente(3, 'Felipe')
bd2.inserir_cliente(4, 'Pedro')
bd2.inserir_cliente(5, 'Guilherme')
# bd.dados é publica
bd2.__dados = 'aaa'
print(bd2.__dados)
bd2.listagem_clientes()
