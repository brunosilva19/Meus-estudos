def entra_de_dados():
    print('OPÇÕES:')
    print('1 - SAUDAÇÃO')
    print('2 - BRONCA')
    print('3 - FELICITAÇÃO')
    print('0 - FIM')
    ops = int(input(''))
    return ops

def escolhas():
    while True:
        ops = entra_de_dados()
        if ops == 1:
            print('1 - Olá. Como vai?')
        elif ops == 2:
            print('2 - Vamos estudar mais.')
        elif ops == 3:
            print('3 - Meus Parabéns!')
        elif ops == 0:
            print('0 - Fim de serviço.')
            break
        else:
            print('Opção inválida.')
def main():
    escolhas()

if __name__ == '__main__':
    main()