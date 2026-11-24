def verificar_valores(nub1, nub2, nub3):
    if nub1 == nub2 == nub3:
        print('Todos os valores são iguais')
    elif nub1 != nub2 and nub1 != nub3 and nub2 != nub3:
        print('Todos os valores são diferentes')
    else:
        print('Existem dois valores iguais e um diferente')


def main():
    try:
        nub1 = int(input())
        nub2 = int(input())
        nub3 = int(input())
    except ValueError:
        print('Entrada inválida. Digite apenas números inteiros')
        return

    verificar_valores(nub1, nub2, nub3)


if __name__ == "__main__":
    main()