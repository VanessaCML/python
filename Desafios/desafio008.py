n = float(input('Digite o valor em metros para a conversão: '))
print(f'{n}m equivale a {n*100:.2f}cm ou a {n*1000:.2f}mm.'
      f'\nNuma escala completa, {n}m também equivale a:'
      f'\n{n/1000:.3f}Km'
      f'\n{n/100:.2f}Hm'
      f'\n{n/10:.2f}Dam'
      f'\ne {n*10:.2f}dm.')

