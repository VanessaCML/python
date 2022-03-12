lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'
pessoa = 'Vanessa', 32, 'F', 56.5
# del (pessoa)  Vai deletar o que está dentro da variável
# print(lanche[-2])
# print (lanche[1:3] = Suco, Pizza
# print (lanche[-2:] = Começa na pizza e vai até o último
# print(sorted(lanche)) = Coloca em ordem (transforma em lista)

'''for comida in lanche:
    print(f'Eu vou de {comida}.')
print('Comi pra caramba!')'''

# Para contabilizar posição:
'''for cont in range(0, len(lanche)):
    print(f'Eu vou de {lanche[cont]} na posição {cont}.')'''
# OU
'''for pos, comida in enumerate(lanche):
    print(f'Eu vou de {comida} na posição {pos}.')'''

a = 3, 6, 9
b = 6, 8, 3, 3
c = b + a
print(c)  # Vai juntar uma com a outra. Primeiro aparece 'a' e depois a tupla 'b'. a + b != b + a
print(c.count(8))  # Mostra quantas vezes aparece o '6' na tupla unificada
print(c.index(3, 4))  # Mostra a posição do '3' na tupla. Ele identifica a primeira que aparece. Dps da ',' pode pedir a posição.

