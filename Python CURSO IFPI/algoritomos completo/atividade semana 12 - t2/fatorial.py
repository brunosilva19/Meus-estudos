def dados():
    return int(input('Digite um número para saber o fatorial: '))


def calculos(num):
    count = 1
    fatorial = 1
    print(f'{'FATORIA':=^52}')

    count_linha = 0

    while count <= num:
        count_linha += 1
        print(f'{count}', end='')
        print(' x ' if count < num else ' = ', end='')
        if count_linha == 10:
            count_linha = 0
        fatorial *= count
        count += 1
    print(fatorial)

def main():
    num = dados()
    print()
    calculos(num)

if __name__ == '__main__':
    main()