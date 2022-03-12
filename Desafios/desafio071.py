# RESOLVENDO DE FORMA MATEMÁTICA:
'''v = int(input('Quanto deseja sacar? R$ '))
c50 = v // 50
c20 = (v % 50) // 20
c10 = ((v % 50) % 20) // 10
c1 = (((v % 50) % 20) % 10) / 1
print(f'Total: {c50:.0f} cédulas de R$ 50.')
print(f'Total: {c20:.0f} cédulas de R$ 20.')
print(f'Total: {c10:.0f} cédulas de R$ 10.')
print(f'Total: {c1:.0f} cédulas de R$ 1.')'''


# RESOLVENDO COM FOR:
'''v = int(input('Valor do saque: R$ '))
for nota in [50, 20, 10, 1]:
    quantidade = v // nota
    v = v % nota
    if quantidade > 0:
        print(f'{quantidade} notas de R$ {nota}')'''

# RESOLVENDO COM WHILE:
v = int(input('Quanto deseja sacar? R$ '))
total = v
cedula = 50
t = 0
while True:
    if total >= cedula:
        total -= cedula
        t += 1
    else:
        if t > 0:
            print(f'{t} cédulas de {cedula}.')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        t = 0
        if total == 0:
            break























