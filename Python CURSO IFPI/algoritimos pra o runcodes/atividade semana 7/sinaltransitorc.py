def ops(valor):
    return valor in ('V', 'A', 'E')

def main():
    valor = input('').strip().upper()
    if ops(valor):
        if valor == 'V':
            print('Siga')
        elif valor == 'A':
            print('Atenção')
        else:
            print('Pare')
    else:
        print('Opção inválida!')
if __name__ == '__main__':
    main()