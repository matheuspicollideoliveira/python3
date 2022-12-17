nome = str(input('Digite seu nome completo:')).strip()
print('\33[0:36mExiste o sobrenome "Silva" nesse nome?\33[m')
print("SILVA" in nome.upper())
