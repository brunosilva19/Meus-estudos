def notas():
    n = float(input('Digite a nota do aluno: '))
    return n
def calcular():
     while True:
        nota = notas()
        if 0 <= nota <= 10:   
            if nota >= 8.5:
                return 'A'
            elif nota >= 7.0:
                return 'B'
            elif nota >= 5.0:
                return 'C'
            elif nota >= 4:
                return 'D'
            else:
                return 'E'
        else:
            print('Nota inválida.')


def main():
    print(f'O aluno receberá:  {calcular()}')


if __name__ == '__main__':
    main()