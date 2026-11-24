def operacoes(operacao, valor1, valor2):
    if operacao == 1:
        return valor1 + valor2
    elif operacao == 2:
        return valor1 - valor2
    elif operacao == 3:
        return valor1 * valor2
    elif operacao == 4:
        return valor1 / valor2
    else:
        raise ValueError('Opção inválida.')
def main():
    try:
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        ops = int(input("""================================
[1] Adição
[2] Subtração
[3] Multiplicação
[4] Divisão
================================
Escolha qual operação: """))
        resultado = operacoes(ops, num1, num2)
        if resultado.is_integer():
            resultado = int(resultado)
            print(f'{resultado}')
        else:
            print(f'{resultado:.2f}')
    except ValueError:
        print('Entrada inválida.')
    except ZeroDivisionError:
        print('Não é possível dividir por zero.')
if __name__ == '__main__':
    main()