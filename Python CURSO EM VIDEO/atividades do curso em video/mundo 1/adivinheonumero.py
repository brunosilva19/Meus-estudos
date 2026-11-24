from random import randint
from time import sleep
pensamento = randint(0, 5)
print('-==-' * 15)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-==-' * 15)
numero = int(input('Qual o número que eu pensei? '))
print('Pensando...')
sleep(2)
if numero == pensamento:
    print('PARABÉNS! Você conseguiu  acertar!')
else:
    print(f'EU GANHEI! Eu pensei no número {pensamento} e não no {numero}!')
