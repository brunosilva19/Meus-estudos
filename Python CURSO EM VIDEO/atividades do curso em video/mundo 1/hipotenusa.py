import math
cateto_o = float(input('Comprimento do cateto oposto: '))
cateto_a = float(input('Comprimento do cateto adjacente: '))

hipotenusa = ((cateto_o ** 2) + (cateto_a ** 2)) ** 0.5
hipotenusa2 = math.sqrt(pow(cateto_a,2) + pow(cateto_o,2))
hipotenusa3 = math.hypot(cateto_o, cateto_a)

print(f'A hipotenusa vai medir {hipotenusa:.2f}' ' = náo foi usado o biblioteca MATH')
print(f'A hipotenusa vai medir {hipotenusa2:.2f}' ' = foi usado a função SQRT() E POW()' )
print(f'A hipotenusa vai medir {hipotenusa3:.2f}' ' = foi usado a função HYPOT()')
