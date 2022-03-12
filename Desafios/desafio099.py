from random import randint
from time import sleep


def maior(*num):
    co = 0
    maior = 0
    t = len(num)
    print(f'Analisando os valores...')
    sleep(1)
    for c in num:
        sleep(0.5)
        print(c, end=' ')
        if co == 0:
           maior = c
        else:
            if c > maior:
                maior = c
        co += 1
    sleep(2)
    print(f'\nFoi informado {t} números.')
    sleep(2)
    print(f'O maior é {maior}.')
    sleep(1)
    print('<>'*15)


maior(randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
maior(randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
maior(randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
maior(randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
maior()
