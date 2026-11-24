def resto_zero(num):
    return 9 * num + 7
def resto_um(num):
    return 'par' if num % 2 == 0 else 'ímpar'
def resto_dois(num):
    return 5 * num**2 - 3 * num + 42
def resto_tres(num):
    return num // 10
def resto_quatro(num):
    return num**2
def valor_por_5(num):
    resto = num % 5

    if resto == 0:
        return resto_zero(num)
    elif resto == 1:
        return resto_um(num)
    elif resto == 2:
        return resto_dois(num)
    elif resto == 3:
        return resto_tres(num)
    else:
        return resto_quatro(num)


def main():
    num = int(input('Digite um valor: '))
    print(valor_por_5(num))


if __name__ == '__main__':
    main()