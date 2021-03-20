"""
# Maneira errada

def move(direction):
    if direction != 'direita' and direction != 'esquerda' and direction != 'frente' and direction != 'trás':
        raise ValueError('Cannot move in this direction!')
    return f'Foi para {direction}'"""
from enum import Enum, auto


class Diretions(Enum):
    esquerda = auto()
    direita = auto()
    cima = auto()
    baixo = auto()


def move(direction):
    if not isinstance(direction, Diretions):
        raise ValueError('Cannot move in this direction!')
    return f'Foi para {direction.name}'


if __name__ == '__main__':
    print(move(Diretions.cima))
    print(move(Diretions.baixo))
    print(move(Diretions.esquerda))
    print(move(Diretions.direita))