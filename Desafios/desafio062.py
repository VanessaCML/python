#RESOLUÇÃO DO PROFESSOR
'''n = int(input('Digite um número inicial:'))
r = int(input('Digite a razão: '))
c = 1
t = n
mais = 10
total = 0
while mais != 0:
    total += mais
    while c <= total:
        print(f'{t} -> ', end='')
        t += r
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer a mais: '))
print(f'FIM. Você visualizou {total} termos.')'''

# Fiz sozinha e incrementei:
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = int(input('Quantos termos deseja ver: '))
c = 1
t = n
mais = termo
total = 0
while mais != 0:
    total += mais
    while c <= total:
        print(f'{t} -> ', end='')
        t += r
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais: '))
print(f'Você viu {total} termos.')
