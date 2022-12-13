r1 = float(input('Reta 1:'))
r2 = float(input('Reta 2:'))
r3 = float(input('Reta 3:'))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('É possível formar um triângulo e ele é ',end = '')
    if r1 == r2 ==r3:
        print('\33[35mEquilátero!')
    if r1 == r2 and r1 != r3 or r1 == r3 and r1 != r2 or r2 == r3 and r2 != r1:
        print('\33[36mIsósceles!')
    if r1 != r2 and r1 !=r3 and r2 != r3:
        print('\33[34mEscaleno!')
    #else:
       #print('Isósceles') Poderia tirar o segundo 'if' e colocar esse 'else'
else:
    print('\33[1:31mNão é possível formar um triângulo!\33[m')