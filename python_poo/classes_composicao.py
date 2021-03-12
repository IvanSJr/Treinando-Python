class Cliente:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.enderecos = []

    def inserir_enderecos(self, cidade, estado, cep):
        self.enderecos.append(Endereco(cidade, estado, cep))  # Composição está sendo realizada aqui

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(f'Cep: {endereco.cep}\nCidade: {endereco.cidade}\nEstado: {endereco.estado}')

    def __del__(self):
        print(f'{self.nome} foi apagado.')


class Endereco:
    def __init__(self, cidade, estado, cep):
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

    def __del__(self):
        print(f'{self.cidade}/{self.estado} foi apagado')


cliente1 = Cliente('Ivan', 20, '800.000.000-64')
cliente1.inserir_enderecos('Lauro de Freitas', 'Bahia', '42739-195')

cliente2 = Cliente('João', 25, '909.020.030-03')
cliente2.inserir_enderecos('Jundiaí', 'São Paulo', '01223-907')
cliente2.inserir_enderecos('Ipanema', 'Rio de Janeiro', '23545-037')


cliente3 = Cliente('Felipe', 18, '800.500.111-11')
cliente3.inserir_enderecos('Salvador', 'Bahia', '42739-195')

# Após a execução tudo é apagado
