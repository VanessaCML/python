a = int(input('Digite um número inteiro: '))
n = int(input('\nDigite 1 para converter para binário'
              '\nDigite 2 para converter para octal'
              '\nDigite 3 para converter para hexadecimal'
              '\nSua opção: '))
if n == 1:
    print(f'\n{a} convertido para binário é igual a {a:b}.') #:b para evitar números negativos
elif n == 2:
    print(f'\n{a} convertido para octal é igual a {oct(a)[2:]}.') #ou {a:o}
elif n == 3:
    print(f'\n{a} convertido para hexadecimal é igual a {hex(a)[2:]}.') #ou {a:h}
else:
    print('\nOPÇÃO INVÁLIDA. TENTE NOVAMENTE.')
