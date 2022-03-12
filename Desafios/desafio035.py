l1 = float(input('Qual o comprimento da primeira reta? '))
l2 = float(input('Qual o comprimento da segunda reta? '))
l3 = float(input('Qual o comprimento da terceira reta? '))
lista = [l1, l2, l3]
ordem = sorted(lista)
print(f'Com essas 3 retas {"não " if ordem[0]+ordem[1]<=ordem[2] else ""}é possível formar um triângulo.')
