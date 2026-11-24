def main():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    n3 = int(input("Digite o terceiro número: "))

    if n1 > n2:
        n1, n2 = n2, n1

    if n1 > n3:
        n1, n3 = n3, n1

    if n2 > n3:
        n2, n3 = n3, n2

    print(n1, n2, n3)
if __name__ == "__main__":
    main()