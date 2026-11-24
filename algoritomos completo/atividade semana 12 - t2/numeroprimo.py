def dados():
    return int(input('Digite um número para saber se ele é primo: '))


def eh_primo_calculo(num):
    count = 0
    primo = 0

    while count < num:
        count += 1
        if num % count == 0:
            primo += 1

    return primo == 2


def main():
    num = dados()
    eh_primo = eh_primo_calculo(num)
    print('=' * 40)
    print(f'O número {num}: ','\033[32mÉ primo\033[m' if eh_primo else '\033[31mNão é primo\033[m')
    print('=' * 40)

if __name__ == '__main__':
    main()