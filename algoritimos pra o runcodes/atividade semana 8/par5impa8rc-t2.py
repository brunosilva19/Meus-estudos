def par(valor):
    return valor % 2 == 0
def main():
    valor = int(input(''))
    resultado = par(valor)
    if resultado:
        print(valor + 5)
    else:
        print(valor + 8)
if __name__ == '__main__':
    main()