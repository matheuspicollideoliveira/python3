frase = str(input('Digite uma frase:')).strip().upper()
print(f'\33[0:32mA letra "a" aparece {frase.count("A")} vezes nesta frase!')
print(f'\33[0:31mA letra "a" aparece pela primeira vez na posição {frase.find("A")+1}!')
print(f'\33[0:33mA letra "a" aparece pela última vez na posição {frase.rfind("A")+1}!')