from random import randint
pensamento_pc = randint(0, 10)
print('''          OI,sou seu computador...
acabei de pensar em um número ente 0 e 10.
Será que você consegue adivinhar qual foi?
''')
usuario = ''
tentativas = 0 
while usuario != pensamento_pc:
    usuario = int(input('Qual o seu palpite? '))
    tentativas += 1
    if usuario > pensamento_pc:
        print('Menos... Tente mais uma vez.')
    elif usuario < pensamento_pc:
        print('Mais... Tente mais uma vez')
print(f'Parabéns o número que eu pensei foi: {pensamento_pc}. \nVocê acertou com: {tentativas} tentativas.')