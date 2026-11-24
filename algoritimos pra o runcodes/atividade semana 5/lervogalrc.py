"""Verifica se o caractere informado é uma vogal."""

valor: str = input('').upper()
print(bool(valor in 'AEIOU'))
