s = str(input('Digite seu sexo (F/M): ')).upper().strip()[0]
while s not in 'MmFf':
    s = str(input('Opção inválida. Digite novamente. Digite seu sexo (F/M): ')).upper().strip()
print(f'Sexo {s} registrado com sucesso.')
