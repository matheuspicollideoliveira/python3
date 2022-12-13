from time import sleep
print('{:=^40}'.format('\33[34mANO NOVO\33[m'))
for c in range(10, 0, -1):
    sleep(1)
    print(c)
print('\33[1:32mFeliz \33[1:31mAno Novo!!!')

