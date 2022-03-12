# HELP INTERACTIVE
help(print)
print(input.__doc__)


# DOCSTRINGS
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: final da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(c, end=' ')
        c += p
    print('FIM!')


help(contador)

# PARÂMETROS OPCIONAIS
def soma(a=0, b=0, c=0):
    soma = a + b + c
    print(f'A soma é igual a {soma}.')


soma(2, 1) #Posso colocar menos argumentos e não vai dar erro.
soma() #Posso colocar nenhum argumento e não vai dar erro.

# ESCOPO DE VARIÁVEIS
def funcao():
    n1 = 4
    print(f'n1 dentro vale {n1}.')


n1 = 2
funcao()
print(f'n1 global vale {n1}.')


def teste(b):
    global a  # faz com que transforme a variável 'a' em global, logo o '5' abaixo será substituido pelo '8'
    a = 8  # variável local (só vale dentro da função teste)
    b += 4  # variável local (só vale dentro da função teste)
    c = 2  # variável local (só vale dentro da função teste)
    print(f'A dentro vale {a}.'
          f'\nB dentro vale {b}.'
          f'\nC dentro vale {c}.')


a = 2
teste(a)  # variável global
print(f'A fora vale {a}.')

# RETORNANDO VALORES
def soma(a=0, b=0, c=0):
    soma = a + b + c
    return soma  # Ideal para pegar o resultado e personalizá-lo da maneira que eu quero, como no print abaixo


r1 = soma(1, 2, 5)
r2 = soma(2, 5)
r3 = soma(9)
print(f'A soma é igual a {r1}, {r2} e {r3}.')

# EXERCÍCIO AULA 20 - FUNÇÕES (PARTE 2)
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é {fatorial(n)}.')
def par(num=0):
    if n % 2 == 0:
        return True
    else:
        return False


n = int(input('Número: '))
print(par(n))
if par(n):
    print('É par')
else:
    print('Não é par')
