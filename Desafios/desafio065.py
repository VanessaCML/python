cont = maior = menor = soma = 0
continuar = ''
while continuar in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    continuar = str(input('Deseja continuar (S/N): ')).strip()
media = soma / cont
print(f'Você digitou {cont} números e a média deles é {media:.2f}.'
      f'\nO maior valor foi {maior} e o menor {menor}.')
