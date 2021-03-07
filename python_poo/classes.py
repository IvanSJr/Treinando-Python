"""
p1 = Pessoa()
p2 = Pessoa()

p1.nome = 'Ivan'
p1.idade = 19
p2.nome = 'João'
print(f'Nome: {p1.nome}\nIdade: {p1.idade}')
"""
from datetime import datetime


class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, altura, comendo=False, falando=False):
        self.nome = nome.title()
        self.idade = idade
        self.altura = altura
        self.comendo = comendo
        self.falando = falando

    def apresentacao(self):
        print(f'Nome: {self.nome}\nIdade: {self.idade}\nAltura: {self.altura}')

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
            return

        if self.falando:
            print(f'{self.nome} já está falando')
            return

        print(f'{self.nome} disse: {assunto}')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return
        print(f'{self.nome} parou de falar')
        self.falando = False

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return
        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return
        print(f'{self.nome} parou de comer')
        self.comendo = False
        self.falando = False

    def data_nascimento(self):
        return f'{self.nome} nasceu em {self.ano_atual - self.idade}'


p1 = Pessoa(nome='ivan', idade=20, altura=1.75)
p2 = Pessoa(nome='João', idade=12, altura=1.60)
p1.apresentacao()
p2.apresentacao()
p1.falar(f'Olá {p2.nome}')
p2.falar(f'Olá {p1.nome}')
p1.parar_falar()
p2.parar_falar()
p1.comer('Uva')
p2.comer('Mamão')

print(p1.data_nascimento())
print(p2.data_nascimento())
