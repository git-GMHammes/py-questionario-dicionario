# Dicionário Perguntas e resposta
import os

perguntas = {
    'Pergunta 1': {  # Chave da Pergunta, nível 1º FOR
        'pergunta': 'Quanto é 2 + 2? ',  # Pergunta nível 2º FOR
        # Resposta nível 2º FOR
        'respostas': {'a': '1', 'b': '4', 'c': '3', 'd': '2'},
        'correta': 'b'
    },
    'Pergunta 2': {  # Chave da Pergunta, nível 1º FOR
        'pergunta': 'Quanto é 2 * 2? ',  # Pergunta nível 2º FOR
        # Resposta nível 2º FOR
        'respostas': {'a': '1', 'b': '4', 'c': '3', 'd': '2'},
        'correta': 'b'
    },
}
# perguntas - Camada principal da matriz

# chavePerguntaNivel1 - Chave da pergunta: 'Pergunta 1{}', 'Pergunta 2{}'
# # # valorPerguntaNivel2 - Valor da pergunta: 'pergunta:'

# chaveRespostasNive2 - Chave da resposta: 'respostas:'
# # # valorRespostaNivel2 - Valor da resposta: ':{v1, v2, v3}'

# .itens() - Retorne os pares de valores-chave do dicionário

continua = 's'
while continua != 'n':
    correta = 0
    print(f'\n Teste de matemática em Python:')
    for chavePerguntaNivel1, valorPerguntaNivel2 in perguntas.items():
        print(f'\n {chavePerguntaNivel1}: {valorPerguntaNivel2["pergunta"]}')
        for chaveRespostasNive2, valorRespostaNivel2 in valorPerguntaNivel2['respostas'].items():
            print(f'[{chaveRespostasNive2}]: {valorRespostaNivel2}')
# ----------------------------------------------------------------------------------------------------------------------
        resposta = input('\n Digite sua resposta: ')
        if resposta == valorPerguntaNivel2['correta']:
            print(
                f'{valorPerguntaNivel2["correta"]}, está CORRETA')
            correta += 1
        else:
            print(f'{resposta},está ERRADA')
    print(f'\n Você acertou {correta}, perguntas!\n')

    continua = input('Deseja continuar? (n/s)')
    # Apresenta um espaço que oculta as respostas acima no terminal
    print('\n' * 10)
    os.system("cls")  # Limpar a tela no terminar, NÃO FUNCIONA no PyCharm
