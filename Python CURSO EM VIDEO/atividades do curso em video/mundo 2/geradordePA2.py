num = int(input('Digite o primeiro terno de uma pa: '))
raz = int(input('Digite a razão da PA: '))
termo = num
cont = 1
quantidade_de_termos = 10
mais = 1
cont_termo = 10
while mais != 0:
    while cont <= quantidade_de_termos:
        print(f'{termo}', end='')
        print(' ➝  ' if cont < quantidade_de_termos else ' ➝  PAUSA ', end='')
        termo += raz
        cont += 1
    mais = int(input('\nQuantos termos você quer a mais: '))
    cont = 1
    quantidade_de_termos = mais
    cont_termo += mais
print(f'Progressão finalizada com {cont_termo} mostrados.')
