def sexo(sexo):
    return sexo == 1

def main():
#entrada de dados
    nome = input('').title().strip()
    ops = int(input())
    if ops in (1 ,2):
        if sexo(ops):
            print(f'Ilmo Sr. {nome}')
        else:
            print(f'Ilma Sra. {nome}')
    else:
        print('Opção inválida!')

if __name__ == '__main__':
    main()
