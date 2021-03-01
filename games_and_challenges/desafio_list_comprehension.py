string = '012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
contador = 10
lista1 = [string[i:i + contador] for i in range(0, len(string), contador)]  # Fatiamento de string com listcomprehension
retorno = '.'.join(lista1)  # Utilizando o join para modificar a lista e junta-la numa string.
print(retorno)
