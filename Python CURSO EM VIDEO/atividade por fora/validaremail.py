# entrada de dados
email: str = input('Digite seu E-mail: ').strip().lower()
# logica de email
usuario = email[:email.find('@')]
dominio = email[email.rfind('@')+1:]

somente_um_arroba = bool(email.count('@') == 1)
espaco_interno = bool(email.count(' ') == 0)
final_email = bool(email[-4:] == ".com")
# saida pra o usuario

print(f'E-mail padronizado: {email}')
print(f'Quantidade de caracteres: {len(email)}')
print(f'Posição do @: {email.find('@')}')
print(f'Usuário: {usuario}')
print(f'domínio: {dominio}')
print(f'Possui exatamente um @? {somente_um_arroba}')
print(f'Não possui espaço interno? {espaco_interno}')
print(f'Termina com .com? {final_email}')

if somente_um_arroba and espaco_interno and final_email:
    print('E-mail válido!')
else:
    print('E-mail invalido!')
