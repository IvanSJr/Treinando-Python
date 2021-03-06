secreta = 'uniDev'
digitadas = []
while True:
    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Você digitou mais de uma letra')
        continue

    digitadas.append(letra)

    if letra in secreta:
        print(f'Você acertou!')
    else:
        print(f'Você errou!')
        digitadas.pop()

    secreto_temporario = ''

    for letra_secreta in secreta:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreta:
        print(f'Que legal você ganhou a palavra secreta era {secreto_temporario}.')
        break
    else:
        print(f'A palavra secreta está assim {secreto_temporario}.')