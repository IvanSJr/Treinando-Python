class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome.title()
        self.idade = idade
        self.nome_da_classe = self.__class__.__name__

    def falar(self):
        if self.nome_da_classe == 'Cliente':
            print(f'O {self.nome_da_classe.lower()} {self.nome} está falando, ele pode comprar.')
        elif self.nome_da_classe == 'Pessoa':
            print(f'A {self.nome_da_classe.lower()} {self.nome} está falando, ela só pode falar.')
        else:
            print(f'O {self.nome_da_classe.lower()} {self.nome} está falando, ele pode estudar.')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nome} está comprando')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nome} está estudando')


class ClienteVip(Cliente):
    def __init__(self, nome, idade, sobrenome):
        super().__init__(nome, idade)
        self.sobrenome = sobrenome.title()

    def falar(self):
        super().falar()  # Utilizando o metodo falar() da classe pai(Cliente). Busca o primeiro metodo que aparecer
        print(f'{self.nome_da_classe.lower()} está executando a função falar')
        print(f'{self.sobrenome}, {self.nome}. Idade: {self.idade}')


# Sobreposição de classes
c1 = ClienteVip('Ivan', 50, 'Santos')
c1.falar()

# cliente1 = Cliente('João', 12)
# aluno1 = Aluno('Ivan', 19)
# p1 = Pessoa('Felipe', 50)
#
# p1.falar()
# aluno1.falar()
# cliente1.falar()
#
# aluno1.estudar()
# cliente1.comprar()
