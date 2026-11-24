lado1 = int(input('Digite a primeira medida: '))
lado2 = int(input('Digite a segunda medida: '))
lado3 = int(input('Digite a terceira medida: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print(f"Com as medidas {lado1}, {lado2}, {lado3} pode ser formado um triângulo:", end=' ')
    if lado1 == lado2 == lado3:
        print('Equilatero')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('Isoceles')
    else:
        print('Escaleno')
else:
    print('Não pode formar um triângulo!')
