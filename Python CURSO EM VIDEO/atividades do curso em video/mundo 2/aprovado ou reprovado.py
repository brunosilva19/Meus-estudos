"""Media para saber se o aluno passou, reprovou ou está em recuperação."""

# Entrada de dados
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Cálculo da média do aluno
media = (nota1 + nota2) / 2

# Condições para verificar o resultado
if media < 5:
    print(
        f"Com as notas {nota1:.1f} e {nota2:.1f}, sua média é de: {media:.1f}.\n"
        "Você está "
        "\033[31mREPROVADO\033[m!"
    )
elif 5 <= media < 7:
    print(
        f"Com as notas {nota1:.1f} e {nota2:.1f}, sua média é de: {media:.1f}.\n"
        "Você está de "
        "\033[33mRECUPERAÇÃO\033[m!"
    )
else:
    print(
        f"Com as notas {nota1:.1f} e {nota2:.1f}, sua média é de: {media:.1f}.\n"
        "Você está de "
        "\033[32mAPROVADO\033[m!"
    )
