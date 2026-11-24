"""jogo do pedra papel e tesoura"""
# entrada de dados
from random import randint
from time import sleep
computador = randint(0, 2)
itens = ['Pedra', 'Papel', 'Tesoura']
jogador = int(input("""Sua opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
Qual é a sua jogada: """))
if jogador not in (0, 1, 2):
    print('Opção invalida, tente novamente!')
else:
    print('JO')
    sleep(0.7)
    print('KEN')
    sleep(0.7)
    print('POO!!!')
    print('-='*20)
    print(f'Você jogou: {itens[jogador]}')
    print(f'O computador jogou: {itens[computador]}')
    print('-='*20)
    # condições para o program
    if jogador == 0 and computador == 2:
        print('\033[32mVocê ganhou!\033[m.')
    elif jogador == 1 and computador == 0:
        print('\033[32mVocê ganhou!\033[m')
    elif jogador == 2 and computador == 1:
        print('\033[32mVocê ganhou!\033[m')
    elif jogador == computador:
        print('\033[34mDeu empate!!!\033[m')
    else:
        print('\033[31mVocê perdeu!\033[m')
