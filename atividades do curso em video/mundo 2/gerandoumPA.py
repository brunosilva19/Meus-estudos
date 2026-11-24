num = int(input('Digite o primeiro terno de uma pa: '))
raz = int(input('Digite a razão da PA: '))
p_t = 10
while p_t > 0:
    print(f'{num}', end='')
    print(' ➝ ' if p_t > 1 else ' ➝  FIM ', end=' ')
    num += raz
    p_t -= 1