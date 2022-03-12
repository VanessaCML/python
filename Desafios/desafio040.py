from time import sleep
print('\33[1;32m=+=\33[m'*7)
print(' \33[1;32mPORTAL DO PROFESSOR\33[m')
print('\33[1;32m=+=\33[m'*7)
sleep(1)
n1 = float(input('\33[1;97mDigite a primeira nota:\33[m '))
n2 = float(input('\33[1;97mDigite a segunda nota:\33[m '))
m = (n1 + n2) / 2
if  n1 > 10 or n1 < 0 or n2 > 10 or n2 < 0:
    print('\n\33[1;31mDigite apenas números entre 0 e 10.\33[m')
else:
    print('\n\33[1;31mPROCESSANDO...\33[m')
    sleep(2)
    if m < 5:
        print(f'\n\33[4;31mREPROVADO\33[m com a média {m:.1f}')
    elif 7 > m >= 5:
        print(f'\n\33[4;33mEM RECUPERAÇÃO\33[m com a média {m:.1f}.')
    elif m >= 7:
        print(f'\n\33[4;36mAPROVADO\33[m com média {m:.1f}.')
