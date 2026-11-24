# jogo do par ou impar
from random import randint
usuario_escolha = input('Escolha (PAR/ ÍMPAR): ').upper()
usuario_numero = int(input('Escolha um número entre 0 e 5: '))
usuario_escolha = usuario_escolha.replace('I', 'Í')
numero_do_computador = randint(0, 5)
soma = usuario_numero + numero_do_computador
# saida pra o usuario
print(f'Número do computador: {numero_do_computador}')
print(f'Soma dos números: {soma}')
resultado = 'PAR' if soma % 2 == 0 else 'ÍMPAR'
print(f'Resultado: {resultado}')
if usuario_escolha == resultado:
    print('Você venceu!')
else:
    print('Você perdeu!')
