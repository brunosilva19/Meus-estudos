def sexo(sexo):
    return sexo == 1

def main():
#entrada de dados
    nome = input('Digite o seu nome: ').title().strip()
    ops = int(input("""=========================
[1] Masculino
[2] Feminino
=========================
Digite [ 1 ] ou [ 2 ]: """))
    print('=========================')
    if ops in (1 ,2):
        if sexo(ops):
            print(f'Ilmo Sr. {nome}')
        else:
            print(f'Ilmo Sra. {nome}')
    else:
        print('Opção inválida!')

if __name__ == '__main__':
    main()
