ext = ('zero', 'um', 'dois', 'três', 'quatro',
       'cinco', 'seis', 'sete', 'oito', 'nove',
       'dez', 'onze', 'doze', 'treze','catorze',
       'quinze', 'dezesseis', 'dezessete', 'dezoito',
       'dezenove', 'vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    while n not in range(0, 21):
        n = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {ext[n]}.')
    o = ' '
    while o not in 'SN':
        o = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if o == 'N':
        break
print('FIM DO PROGRAMA')
