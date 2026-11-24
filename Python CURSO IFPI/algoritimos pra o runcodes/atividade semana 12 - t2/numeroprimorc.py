def dados():
    return int(input(''))


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
    print(eh_primo)


if __name__ == '__main__':
    main()