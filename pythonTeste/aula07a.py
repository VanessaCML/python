nome = input('Qual o seu nome? ')
print(f'Prazer em te conhecer, {nome:20}.')
print(f'Prazer em te conhecer, {nome:^20}.')
print(f'Prazer em te conhecer, {nome:>20}.')
print(f'Prazer em te conhecer, {nome:_^20}.')

a = int(input('Digite um numero: '))
b = int(input('Digite outro: '))
s = a + b
m = a * b
d = a / b
di = a // b
e = a ** b
print(f'A soma é {s}, \no produto é {m}, \na divisão é {d:.3f},', end=' -> ')
print(f'a divisão inteira é {di} \ne a potência é {e}.')








