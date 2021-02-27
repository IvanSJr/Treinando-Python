perguntas = {
    'Pergunta 1': dict(pergunta='Qual a raiz quadradade de 4?', respostas={'a': '1', 'b': '4', 'c': '8', 'd': '2'},
                       resposta_certa='d'),
    'Pergunta 2': dict(pergunta='Qual o resultado da equação 2*5/2+10?',
                       respostas={'a': '15', 'b': '1,2', 'c': '20', 'd': '10'}, resposta_certa='a'),
    'Pergunta 3': dict(pergunta='Qual a raiz quadradade de 144', respostas={'a': '288', 'b': '4', 'c': '12', 'd': '20'},
                       resposta_certa='c'),
    'Pergunta 4': dict(pergunta='Quem descobriu o Brasil?',
                       respostas={'a': 'Os Índios', 'b': 'Bolsonaro', 'c': 'Pedro Alvarez Cabral',
                                  'd': 'Rei Dom Manuel'}, resposta_certa='c'),
    'Pergunta 5': dict(pergunta='Qual o valor de PI?', respostas={'a': '1,44', 'b': '3,13', 'c': '3,14', 'd': '6.66'},
                       resposta_certa='c'),
    'Pergunta 6': dict(pergunta='Quem é a deusa Egipcia com forma de gato, que é ligada fertilidade?',
                       respostas=dict(a='Nut', b='Hathor', c='Anúbis', d='Bastet'), resposta_certa='d'),
    'Pergunta 7': dict(pergunta='Segundo a mitologia grega como o deus Odin criou o mundo?',
                       respostas={'a': 'Do pó das estrelas', 'b': 'Equilibrando a luz e as trevas', 'c': 'Do nada',
                                  'd': 'Do corpo de um gigante'}, resposta_certa='d'),
    'Pergunta 8': dict(pergunta='Qual o nome do martelo mágico do deus Thor?',
                       respostas=dict(a='Mjollinir', b='Jorojomund', c='Frarknium', d='Dunveldrenvarden'),
                       resposta_certa='a'),
    'Pergunta 9': dict(pergunta='Qual deus da mitologia grega é conhecido como "pai de todos"?',
                       respostas=dict(a='Loki', b='Thor', c='Odin', d='Fafnir'), resposta_certa='c'),
    'Pergunta 10': dict(pergunta='Como eram chamadas as guerreiras de Odin, encarregadas de levar as almas dos '
                                 'guerreiros até o palácio Valhalla?',
                        respostas=dict(a='Amazonas', b='Damas da Noite', c='Anjos', d='Valquírias'), resposta_certa='d')
}

resp_c = 0
for pk, pv in perguntas.items():
    print(f'{pk} {pv["pergunta"]}')

    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv} ')

    resposta_usuario = input('Sua Resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print('Você acertou')
        resp_c += 1
    else:
        print('Você errou!')
    print()

print(f'Você acertou {resp_c} alternativas!')