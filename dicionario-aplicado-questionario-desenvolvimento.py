# questionario - Nivel raíz do Dicionário das perguntas e respostas
# Pergunta N - Chave que divide as matrizes das perguntas do nivel [1] FOR
# pergunta - Pergunta do subnível [2] do FOR
# respostas - resposta do subnível [2] do FOR
# resposta - resposta do subnível [2] do FOR
# correta - resultado do subnível [2] do FOR
# incorreta - resultado do subnível [2] do FOR

questionario = {  # Não entra no FOR
    'Pergunta 1': {  # Vou chamar de [Resposta_1] no Nivel 1 do FOR
        # Vou chamar de [pergunta] Nível 1 e 2 do FOR
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {  # Vou chamar de [respostas] no Nivel 2 do FOR
            'a': '2',  # Vou chamar de [resposta] como valor no nível 2
            'b': '4',
            'c': '3',
            'd': '5'
        },
        'correta': 'b'
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 2*2? ',
        'respostas': {
            'a': '4',
            'b': '2',
            'c': '5',
            'd': '3'
        },
        'correta': 'a'
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 3x5? ',
        'respostas': {
            'a': '11',
            'b': '35',
            'c': '08',
            'd': '15',
        },
        'correta': 'd'
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é 6x6? ',
        'respostas': {
            'a': '36',
            'b': '12',
            'c': '66',
            'd': '33',
        },
        'correta': 'a'
    },
    'Pergunta 5': {
        'pergunta': 'Quanto é 6x3? ',
        'respostas': {
            'a': '09',
            'b': '12',
            'c': '18',
            'd': '24',
        },
        'correta': 'c'
    },

}
print('\n Teste de matemática em Python!')
correta = 0
incorreta = 0
for Pergunta_1, pergunta in questionario.items():  # Pergunta 1, pergunta e questionario
    print(f'\n {Pergunta_1}: {pergunta["pergunta"]}')
    # respostas (chave:), resposta (:valor), pergunta['respostas']
    for respostas, resposta in pergunta['respostas'].items():
        print(f'{respostas}: {resposta}')
    # ------------------------------------------------------------------------------------------------------
    respostaUsuario = input('\n Qual a letra que corresponde a resposta? ')
    if respostaUsuario == pergunta['correta']:
        print(f' {pergunta["correta"]} - Está correto!')
        correta += 1
    else:
        print(f'{respostaUsuario}, está errada.')
        incorreta += 1
    # ------------------------------------------------------------------------------------------------------
print(f'\n resultado: {correta}, acertos')
print(f'\n resultado: {incorreta}, erros')
