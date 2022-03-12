def l():
    print('~' * 30)


def soma(a, b):
    l()
    print(f'A = {a} e B = {b}.')
    s = a + b
    print(f'A soma de A + B é igual a {s}.')
    l()


# Programa principal:
a = 4
b = 5
s = a + b
print(s)
# Pode ser substituído por: def no início do programa e:
soma(a=4, b=5)
soma(b=8, a=5)
soma(a=2, b=1)


# Desempacotando parâmetros: (recebe argumentos à vontade durante o código)
def contador(*num):
    c = 0
    tamanho = len(num)
    for valor in num:
        print(valor, end=', ' if c < tamanho - 1 else '. ')
        c += 1
    print(f'Recebi os valores {num} dando no total {tamanho} valores.')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


# Trabalhando com listas, não é necessário desempacotar parâmetros:
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


print()
valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)
print()


def soma(* numeros):
    s = 0
    for v in numeros:
        s += v
    print(f'A soma dos valores é de {s}.')


soma(2, 5)
soma(2, 9, 4)

