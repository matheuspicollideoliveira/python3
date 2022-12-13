print('\33[32mOs números pares entre 0 e 50 são:\33[m')
for c in range(2, 51):
    if c % 2 == 0:
        print(c, end=' ')
#ou

#for c in range(2, 51, 2):
    #print(c, end=' ')