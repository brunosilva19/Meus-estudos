from random import randint

print('≡' * 56)
print(f'{"VAMOS JOGAR PAR OU ÍMPAR":^56}')
print('≡' * 56)
vitorias = 0
while True:
    computador = randint(1, 10) # o computador randomiza um valor
    jogador = int(input('Que número você escolhe: ')) # o jogador escolher um valor
    tipo = ' '
    while tipo not in 'PI':
        tipo = input('PAR OU ÍMPAR?[ P / I ]: ').upper().strip()[0] # o jogador escolher par ou ímpar
    print('≡' * 60)
    
    resultado = computador + jogador # soma os valores 
    
    valor = 'DEU PAR' if resultado % 2 == 0 else 'DEU ÍMPAR' # imprime o texto par ou ímpar de pendendo do resultado do resto da divisão por 2
    
    print()
    print(f'Você jogou {jogador} e o computador jogou {computador}. O total de {resultado} {valor}')
    print()
    print('≡' * 60)
    
    if tipo == 'P' and resultado % 2 == 0:
        print('\033[32mVocê VENCEU!\033[m')
        vitorias += 1
        
    elif tipo == 'I' and resultado % 2 != 0:
        print('\033[32mVocê VENCEU!\033[m')
        vitorias += 1
        
    else:
        print(f'\033[31m{"Você PERDEU!":^60}\033[m')
        break
    
    print('Vamos jogar novamente...')
    print('≡' * 60)
print('≡' * 60)
print(f'\033[31mGAME OVER!\033[m Você venceu: {vitorias}')
print()
print('≡' * 60)
