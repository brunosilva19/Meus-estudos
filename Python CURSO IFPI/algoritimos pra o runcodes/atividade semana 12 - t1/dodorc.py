def dados():
    return int(input(''))

def calculos(quantidade_dodo):
    LIMITE_POPULACIONAL = quantidade_dodo * 0.1
    quantidade_dodo_atual = quantidade_dodo_vivos = quantidade_dodo_mortos = 0
    ano = 1600

    while quantidade_dodo >= LIMITE_POPULACIONAL:
        quantidade_dodo_atual = quantidade_dodo - quantidade_dodo * 0.05
        quantidade_dodo_vivos = quantidade_dodo * 0.01
        quantidade_dodo_mortos = quantidade_dodo * 0.06
        quantidade_dodo = quantidade_dodo_atual
        print(f'{ano},{quantidade_dodo_vivos:.0f},{quantidade_dodo_mortos:.0f},{quantidade_dodo_atual:.0f}')
        ano += 1

def main():
    quantidade_dodo = dados()
    calculos(quantidade_dodo)

if __name__ == '__main__':
    main()