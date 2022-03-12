from random import randint
n = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
print(f'Os números sorteados foram: ', end='')
for num in n:
    print(num, end=' ')
print(f'\nO menor número é {min(n)} e o maior é {max(n)}.')


'''from random import randint
a = tuple(randint(1, 5) for i in range(5))

print(f'Os números sorteados foram {a}, o maior é {max(a)} e o menor é {min(a)}.')'''

