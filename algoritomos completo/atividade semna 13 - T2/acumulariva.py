def lista():
    return []

def receber_valores(lista_principal):
    while True:
        num = int(input('Divite um valor: [0 para encerrar o programa] '))
        if num == 0:
            break
        lista_principal.append(num)

def soma_acumulativa(lista_principal):
    total = 0
    lista_secundaria = []
    for c in lista_principal:
        total += c
        lista_secundaria.append(total)
    return lista_secundaria
        
def main():
    lista_principal = lista()
    receber_valores(lista_principal)
    print(soma_acumulativa(lista_principal))

if __name__ == '__main__':
    main()