n = int(input('Quantos termos deseja ver: '))
c = 3
t1 = 0
t2 = 1
print(f'{t1} -> {t2} -> ', end='')
while c <= n:
    total = t1 + t2
    print(f'{total} -> ', end='')
    t1 = t2
    t2 = total
    c += 1
print('FIM')
