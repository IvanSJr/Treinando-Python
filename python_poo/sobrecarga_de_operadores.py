class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def mostrar_retangulo(self):
        print(f'Altura: {self.altura}\nLargura: {self.largura}')

    def get_area(self):
        return self.altura * self.largura

    def __add__(self, other):
        novo_altura = self.altura + other.altura
        nova_largura = self.largura + other.largura
        return Retangulo(novo_altura, nova_largura)

    # Checando > é maior
    def __gt__(self, other):
        """
        :param other: Retangulo que será comparado
        :return: Retorna qual é o maior.
        """
        l1 = self.get_area()
        l2 = other.get_area()
        if l1 > l2:
            return True
        return False

    # Checando < é menor
    def __lt__(self, other):
        """
        :param other: Retangulo que será comparado
        :return: Retorna qual é o menor.
        """
        l1 = self.get_area()
        l2 = other.get_area()
        if l1 < l2:
            return True
        return False

    # Checando == é igual
    def __eq__(self, other):
        """
        :param other: Retangulo que será comparado.
        :return: Verifica se são iguais.
        """
        if self.altura == other.altura and self.largura == other.largura:
            return True
        return False


r1 = Retangulo(30, 20)
r2 = Retangulo(30, 20)
print(r1 == r2)
