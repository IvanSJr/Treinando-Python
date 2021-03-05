# Módulos Padrões do Python
# Módulos são arquivos .py e servem para expandiar as funcionalidades além do padrão da linguagem.
# Os módulos ficam em https://docs.python.org/3/py-modindex.html

from sys import platform
from random import randint

print(platform)  # win32

for i in range(1, 10):
    """ 
    7
    3
    10
    8
    7
    2
    2
    3
    9
    """
    print(randint(1, 10))

